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