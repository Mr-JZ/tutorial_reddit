from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

openapi_schema = {
    "openapi": "3.0.2",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/login": {
            "post": {
                "tags": [
                    "Authentication"
                ],
                "summary": "Login",
                "operationId": "login_login_post",
                "requestBody": {
                    "content": {
                        "application/x-www-form-urlencoded": {
                            "schema": {
                                "$ref": "#/components/schemas/Body_login_login_post"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/": {
            "get": {
                "tags": [
                    "Web Tutorial"
                ],
                "summary": "Main",
                "operationId": "main__get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                }
            }
        },
        "/user/": {
            "get": {
                "tags": [
                    "User"
                ],
                "summary": "Read User",
                "operationId": "read_user_user__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Id",
                            "type": "integer"
                        },
                        "name": "id",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Identification",
                            "type": "string"
                        },
                        "name": "identification",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/User"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "put": {
                "tags": [
                    "User"
                ],
                "summary": "Update User",
                "operationId": "update_user_user__put",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "post": {
                "tags": [
                    "User"
                ],
                "summary": "Create User",
                "operationId": "create_user_user__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/UserCreate"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/User"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            },
            "delete": {
                "tags": [
                    "User"
                ],
                "summary": "Delete User",
                "operationId": "delete_user_user__delete",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "User Id",
                            "type": "integer"
                        },
                        "name": "user_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            }
        },
        "/user/list/": {
            "get": {
                "tags": [
                    "User"
                ],
                "summary": "Read Users",
                "operationId": "read_users_user_list__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Skip",
                            "type": "integer",
                            "default": 0
                        },
                        "name": "skip",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Limit",
                            "type": "integer",
                            "default": 100
                        },
                        "name": "limit",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Read Users User List  Get",
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/User"
                                    }
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/tutorial/": {
            "get": {
                "tags": [
                    "Tutorial"
                ],
                "summary": "Read Tutorial",
                "operationId": "read_tutorial_tutorial__get",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Id",
                            "type": "integer"
                        },
                        "name": "id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Tutorial"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": [
                    "Tutorial"
                ],
                "summary": "Update Tutorial",
                "operationId": "update_tutorial_tutorial__put",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Id",
                            "type": "integer"
                        },
                        "name": "id",
                        "in": "query"
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TutorialCreate"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "202": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Tutorial"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "post": {
                "tags": [
                    "Tutorial"
                ],
                "summary": "Create Tutorial",
                "operationId": "create_tutorial_tutorial__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TutorialCreate"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Tutorial"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "delete": {
                "tags": [
                    "Tutorial"
                ],
                "summary": "Delete Tutorial",
                "operationId": "delete_tutorial_tutorial__delete",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Id",
                            "type": "integer"
                        },
                        "name": "id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "204": {
                        "description": "Successful Response"
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            }
        },
        "/tutorial/list/": {
            "get": {
                "tags": [
                    "Tutorial"
                ],
                "summary": "Read Tutorials",
                "operationId": "read_tutorials_tutorial_list__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Skip",
                            "type": "integer",
                            "default": 0
                        },
                        "name": "skip",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Limit",
                            "type": "integer",
                            "default": 100
                        },
                        "name": "limit",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Name",
                            "type": "string"
                        },
                        "name": "name",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Level",
                            "type": "integer"
                        },
                        "name": "level",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Topic Id",
                            "type": "integer"
                        },
                        "name": "topic_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Read Tutorials Tutorial List  Get",
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/Tutorial"
                                    }
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/vote/": {
            "get": {
                "tags": [
                    "Vote"
                ],
                "summary": "Read Vote",
                "operationId": "read_vote_vote__get",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Id",
                            "type": "integer"
                        },
                        "name": "id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Vote"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": [
                    "Vote"
                ],
                "summary": "Update Vote",
                "operationId": "update_vote_vote__put",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "post": {
                "tags": [
                    "Vote"
                ],
                "summary": "Create Vote",
                "operationId": "create_vote_vote__post",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Tutorial Id",
                            "type": "integer"
                        },
                        "name": "tutorial_id",
                        "in": "query"
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/VoteCreate"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Vote"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "delete": {
                "tags": [
                    "Vote"
                ],
                "summary": "Delete Vote",
                "operationId": "delete_vote_vote__delete",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Vote Id",
                            "type": "integer"
                        },
                        "name": "vote_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            }
        },
        "/vote/list/": {
            "get": {
                "tags": [
                    "Vote"
                ],
                "summary": "Read Votes",
                "operationId": "read_votes_vote_list__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Skip",
                            "type": "integer",
                            "default": 0
                        },
                        "name": "skip",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Limit",
                            "type": "integer",
                            "default": 100
                        },
                        "name": "limit",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Tutorial Id",
                            "type": "integer"
                        },
                        "name": "tutorial_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Vote"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/vote/login/": {
            "get": {
                "tags": [
                    "Vote"
                ],
                "summary": "Read Vote",
                "operationId": "read_vote_vote_login__get",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Id",
                            "type": "integer"
                        },
                        "name": "id",
                        "in": "query"
                    },
                    {
                        "required": True,
                        "schema": {
                            "title": "Tutorial Id",
                            "type": "integer"
                        },
                        "name": "tutorial_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Vote"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            }
        },
        "/vote/login/list/": {
            "get": {
                "tags": [
                    "Vote"
                ],
                "summary": "Read Votes",
                "operationId": "read_votes_vote_login_list__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Skip",
                            "type": "integer",
                            "default": 0
                        },
                        "name": "skip",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Limit",
                            "type": "integer",
                            "default": 100
                        },
                        "name": "limit",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "User Id",
                            "type": "boolean",
                            "default": False
                        },
                        "name": "user_id",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Tutorial Id",
                            "type": "integer"
                        },
                        "name": "tutorial_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Vote"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            }
        },
        "/video/": {
            "get": {
                "tags": [
                    "Video"
                ],
                "summary": "Read Video",
                "operationId": "read_video_video__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Id",
                            "type": "integer"
                        },
                        "name": "id",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Url",
                            "type": "string"
                        },
                        "name": "url",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Name",
                            "type": "string"
                        },
                        "name": "name",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Video"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": [
                    "Video"
                ],
                "summary": "Update Video",
                "operationId": "update_video_video__put",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "post": {
                "tags": [
                    "Video"
                ],
                "summary": "Create Video",
                "operationId": "create_video_video__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/VideoCreate"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Video"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "delete": {
                "tags": [
                    "Video"
                ],
                "summary": "Delete Video",
                "operationId": "delete_video_video__delete",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Video Id",
                            "type": "integer"
                        },
                        "name": "video_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            }
        },
        "/video/list/": {
            "get": {
                "tags": [
                    "Video"
                ],
                "summary": "Read Videos",
                "operationId": "read_videos_video_list__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Skip",
                            "type": "integer",
                            "default": 0
                        },
                        "name": "skip",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Limit",
                            "type": "integer",
                            "default": 100
                        },
                        "name": "limit",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Name",
                            "type": "string"
                        },
                        "name": "name",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Video"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/topic/": {
            "get": {
                "tags": [
                    "Topic"
                ],
                "summary": "Read Topic",
                "operationId": "read_topic_topic__get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Id",
                            "type": "integer"
                        },
                        "name": "id",
                        "in": "query"
                    },
                    {
                        "required": False,
                        "schema": {
                            "title": "Name",
                            "type": "string"
                        },
                        "name": "name",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Topic"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": [
                    "Topic"
                ],
                "summary": "Update Topic",
                "operationId": "update_topic_topic__put",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "post": {
                "tags": [
                    "Topic"
                ],
                "summary": "Create Topic",
                "operationId": "create_topic_topic__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/TopicCreate"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Topic"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            },
            "delete": {
                "tags": [
                    "Topic"
                ],
                "summary": "Delete Topic",
                "operationId": "delete_topic_topic__delete",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Topic Id",
                            "type": "integer"
                        },
                        "name": "topic_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {}
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "OAuth2PasswordBearer": []
                    }
                ]
            }
        },
        "/topic/list/": {
            "get": {
                "tags": [
                    "Topic"
                ],
                "summary": "Read Topics",
                "operationId": "read_topics_topic_list__get",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Skip",
                            "type": "integer"
                        },
                        "name": "skip",
                        "in": "query"
                    },
                    {
                        "required": True,
                        "schema": {
                            "title": "Limit",
                            "type": "integer"
                        },
                        "name": "limit",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Topic"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "Body_login_login_post": {
                "title": "Body_login_login_post",
                "required": [
                    "username",
                    "password"
                ],
                "type": "object",
                "properties": {
                    "grant_type": {
                        "title": "Grant Type",
                        "pattern": "password",
                        "type": "string"
                    },
                    "username": {
                        "title": "Username",
                        "type": "string"
                    },
                    "password": {
                        "title": "Password",
                        "type": "string"
                    },
                    "scope": {
                        "title": "Scope",
                        "type": "string",
                        "default": ""
                    },
                    "client_id": {
                        "title": "Client Id",
                        "type": "string"
                    },
                    "client_secret": {
                        "title": "Client Secret",
                        "type": "string"
                    }
                }
            },
            "HTTPValidationError": {
                "title": "HTTPValidationError",
                "type": "object",
                "properties": {
                    "detail": {
                        "title": "Detail",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        }
                    }
                }
            },
            "Topic": {
                "title": "Topic",
                "required": [
                    "name",
                    "id",
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "name": {
                        "title": "Name",
                        "type": "string"
                    },
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "user_id": {
                        "title": "User Id",
                        "type": "integer"
                    }
                }
            },
            "TopicCreate": {
                "title": "TopicCreate",
                "required": [
                    "name"
                ],
                "type": "object",
                "properties": {
                    "name": {
                        "title": "Name",
                        "type": "string"
                    }
                }
            },
            "Tutorial": {
                "title": "Tutorial",
                "required": [
                    "name",
                    "level",
                    "topic_id",
                    "id",
                    "creator",
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "name": {
                        "title": "Name",
                        "type": "string"
                    },
                    "level": {
                        "title": "Level",
                        "type": "integer"
                    },
                    "topic_id": {
                        "title": "Topic Id",
                        "type": "integer"
                    },
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "creator": {
                        "title": "Creator",
                        "type": "integer"
                    },
                    "user_id": {
                        "title": "User Id",
                        "type": "integer"
                    }
                }
            },
            "TutorialCreate": {
                "title": "TutorialCreate",
                "required": [
                    "name",
                    "level",
                    "topic_id"
                ],
                "type": "object",
                "properties": {
                    "name": {
                        "title": "Name",
                        "type": "string"
                    },
                    "level": {
                        "title": "Level",
                        "type": "integer"
                    },
                    "topic_id": {
                        "title": "Topic Id",
                        "type": "integer"
                    },
                    "description": {
                        "title": "Description",
                        "type": "string"
                    }
                }
            },
            "User": {
                "title": "User",
                "required": [
                    "identification",
                    "id",
                    "is_active"
                ],
                "type": "object",
                "properties": {
                    "identification": {
                        "title": "Identification",
                        "type": "string"
                    },
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "is_active": {
                        "title": "Is Active",
                        "type": "boolean"
                    },
                    "acces_level": {
                        "title": "Acces Level",
                        "type": "integer",
                        "default": 0
                    }
                }
            },
            "UserCreate": {
                "title": "UserCreate",
                "required": [
                    "identification",
                    "password"
                ],
                "type": "object",
                "properties": {
                    "identification": {
                        "title": "Identification",
                        "type": "string"
                    },
                    "password": {
                        "title": "Password",
                        "type": "string"
                    }
                }
            },
            "ValidationError": {
                "title": "ValidationError",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "type": "object",
                "properties": {
                    "loc": {
                        "title": "Location",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "msg": {
                        "title": "Message",
                        "type": "string"
                    },
                    "type": {
                        "title": "Error Type",
                        "type": "string"
                    }
                }
            },
            "Video": {
                "title": "Video",
                "required": [
                    "name",
                    "url",
                    "id"
                ],
                "type": "object",
                "properties": {
                    "name": {
                        "title": "Name",
                        "type": "string"
                    },
                    "url": {
                        "title": "Url",
                        "type": "string"
                    },
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    }
                }
            },
            "VideoCreate": {
                "title": "VideoCreate",
                "required": [
                    "name",
                    "url"
                ],
                "type": "object",
                "properties": {
                    "name": {
                        "title": "Name",
                        "type": "string"
                    },
                    "url": {
                        "title": "Url",
                        "type": "string"
                    }
                }
            },
            "Vote": {
                "title": "Vote",
                "required": [
                    "up",
                    "id",
                    "tutorial_id",
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "up": {
                        "title": "Up",
                        "type": "boolean"
                    },
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "tutorial_id": {
                        "title": "Tutorial Id",
                        "type": "integer"
                    },
                    "user_id": {
                        "title": "User Id",
                        "type": "integer"
                    }
                }
            },
            "VoteCreate": {
                "title": "VoteCreate",
                "required": [
                    "up"
                ],
                "type": "object",
                "properties": {
                    "up": {
                        "title": "Up",
                        "type": "boolean"
                    }
                }
            }
        },
        "securitySchemes": {
            "OAuth2PasswordBearer": {
                "type": "oauth2",
                "flows": {
                    "password": {
                        "scopes": {},
                        "tokenUrl": "login"
                    }
                }
            }
        }
    }
}

def test_docs_change():
    request = client.get("/openapi.json")
    assert request.status_code == 200
    assert request.json() == openapi_schema
