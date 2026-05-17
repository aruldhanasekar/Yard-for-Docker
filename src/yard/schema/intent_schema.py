INTENT_TOOLS = [
  {
      "type" : "function",
      "function" : {
          "name" : "create_dockerfile",
          "description": "Extract creating dockerfile tasks with files and folders",
          "strict" : True,
          "parameters" : {
              "type" : "object",
              "properties" : {
                  "task" : {
                      "type" : "string",
                      "enum" : ["create_dockerfile"]
                  },
                  "runnable" : {
                      "type" : "array",
                      "items" : {
                          "type" : "object",
                          "properties" : {
                              "file" : {
                                  "type" : ["string", "null"]
                              },
                              "folder" : {
                                  "type" : ["string", "null"]
                              }
                          },
                          "required" : ["file", "folder"],
                          "additionalProperties" : False
                      }
                  }
              },
              "required" : [
                  "task",
                  "runnable"
              ],
              "additionalProperties" : False
          }
      }
  },
  {
        "type" : "function",
        "function": {
            "name" : "create_dockerignore",
            "description" : "Extract files and folders to ignore and Create a .dockerignore file",
            "strict" : True,
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "task" : {
                        "type" : "string",
                        "enum" : ["create_dockerignore"]
                    },
                    "ignored": {
                        "type" : "array",
                        "items" : {
                            "type" : "string"
                        },
                        "description" : "ingored files and folders"
                    } 
                },
                "required" : ["task","ignored"],
                "additionalProperties" : False
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "non_docker_request",
        "description": "Use this when the request is not related to Docker or DevOps",
        "strict": True,
        "parameters": {
        "type": "object",
        "properties": {
            "message": {
            "type": "string",
            "enum": [
                "I am a specialized Docker DevOps Engineer. Provide tasks related to Docker."
            ]
            }
        },
        "required": ["message"],
        "additionalProperties": False
        }
    }
    }
]