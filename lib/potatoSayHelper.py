import os

class potatoSayHelper:
    def __init__(self, config, debug):
        self.config = config
        self.debug = debug

    def setCommand(self, sentCommand):
        command = "curl -s -X POST " + self.config['skelly_api'] + "/setCommand -H 'Content-Type: application/json'  -d '{\"command\":\"#SayThis#" + sentCommand + "\"}'"
        resp = os.popen(command).read()

        print(resp) if self.debug == 1 else None

        return True

    ### CHECKS FOR APPOSTROPHIES and replaces phonetics
    def refine_text(self, body):
        ## Catch bad type
        if "'" in body:
            print('Appostrophies do not work currently, rewrite the body')
            exit()

        if "katara" in body.lower():
            newBody = body.replace("katara", "cuh tara")
        else:
            newBody = body

        return newBody

    ## CHECKS INPUTS FROM CLI
    def validate_inputs(self, args):
        try:
            body = args[1]
        except:
            print("ERROR: no body")
            exit()

        try:
            title = args[2]
        except:
            title = body.lower()

        if self.debug == 1:
            print("BODY: " + body)
            print("TITLE: " + title)

        validated_body = self.refine_text(body)
        return (validated_body, title)
