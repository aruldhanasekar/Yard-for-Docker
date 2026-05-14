INTENT_TOOLS = [
  {
      "type" : "function",
      "function" : {
          "name" : "create_dockerfile",
          "description": "Extract creating dockerfile tasks with files and folders",
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
      "function" : {
          "name" : "create_dockerignore",
          "description" : "Extract create .dockeringore task with files, and folders",
          "parameters" : {
              "type" : "object",
              "properties" : {
                  "task" : {
                      "type" : "string",
                      "enum" : ["create_.dockerignore"]
                  },
                  "ignore" : {
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
              "required" : ["task", "ignore"],
              "additionalProperties" : False
          }
      }
  }
]