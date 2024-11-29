import http.client

class NTFY:
  def __init__(self, config):
    self.printer = config.get_printer()
    self.gcode = self.printer.lookup_object('gcode')

    self.ntfyHost = config.get('ntfyHost', 'https://ntfy.sh')
    self.ntfyTopic = config.get('ntfyTopic', 'Klipper')

    self.gcode.register_command(
      'SEND_NTFY', self.cmd_SEND_NTFY, desc=self.cmd_SEND_NTFY_help)

  cmd_SEND_NTFY_help = "Sends a notification to a topic on a specific nfty.sh server"
  def cmd_SEND_NTFY(self, gcmd):

    data = gcmd.get('BODY', "You should really set what this message says.")
    headers = {
      "Title": gcmd.get('TITLE', "3D Printer is talking"),
      "Priority": gcmd.get('PRIORITY', 3),
      "Tags": gcmd.get('TAGS', "expressionless")
    }

    conn = http.client.HTTPSConnection(self.ntfyHost, 443, timeout=10)
    conn.request("POST","/"+self.ntfyTopic, data, headers=headers)

    response = conn.getresponse()
    print("Status: {} and reason: {}".format(response.status, response.reason))

    conn.close()

def load_config(config):
  return NTFY(config)
