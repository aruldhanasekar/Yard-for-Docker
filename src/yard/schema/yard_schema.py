TOOLS = [
    {
        "type" : "function",
        "function" : {
            "name" : "create_dockerfile",
            "description" : "Create a Dockerfile using given information",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "dockerfiles" : {
                        "type" : "array",
                        "items" : {
                            "type" : "object",
                            "properties" : {
                                "dockerfile_name" : {
                                    "type" : "string"
                                },
                                "dockerfile_instructions" : {
                                    "type" : "string"
                                }
                            },
                            "required" : ["dockerfile_name", "dockerfile_instructions"],
                            "additionalProperties" : False
                        }
                    }
                },
                "required" : ["dockerfiles"],
                "additionalProperties" : False
            }
        }
    }
]