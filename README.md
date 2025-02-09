# Toturial Reddit

We use the pricipal to up and down vote a post that is one or multiple videos in a playlist

# Database Tables

### topic
| id  | name |
|-----|------|
| int | str  |

### tutorial
| id  |name|description|topic_id|level|creator|
|-----|----|-----------|--------|-----|-------|
| int | str | str| int| int| int|

### video
| id  | name | url |
|-----|------|-----|
| int | str  | str |

### user
| id  | identification | hashed_password | is_active | access_level |
|-----|----------------|-----------------|-----------|--------------|
| int | str            | str             | bool      | int          |

### vote
| id  | tutorial_id | user_id | up   |
|-----|-------------|---------|------|
| int | int         | int     | bool |

# Install

## Create secrets.json and role.json

If you have nix installed you can use the nix shell to create the files.
```bash
nix develop
```

If you don't have nix installed make sure you have `openssl` installed.

After that you can just run the setup script.

```bash
./setup.sh
```

This will create the files `secrets.json` and `role.json` in the current directory.

## Docker 

to build the image run in the project folder

```
docker build -t tutorial_reddit .
```

if you want to run the container implement the resources from the api into the docker container. You have to change in the resouce folder before you can run the command belowe.

```
docker run -d --name tutred -p 7000:7000 --env "TUTORIAL_REDDIT_SECRET=$(<./secrets.json)" --env "TUTORIAL_REDDIT_ROLE=$(<./role.json)" tutorial_reddit
```
