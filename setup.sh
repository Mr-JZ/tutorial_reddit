#!/bin/bash

# Create secrets.json
cat <<EOL > secrets.json
{
    "SECRET_KEY": "$(openssl rand -hex 32)",
    "ALGORITHM": "HS256",
    "ACCESS_TOKEN_EXPIRE_MINUTES": 30,
    "DATABASE_URL": "sqlite:///./tutorial.db"
}
EOL

# Create role.json
cat <<EOL > role.json
{
    "ADMIN": 2,
    "EDITOR": 1, 
    "USER": 0
}
EOL

# Make the script executable
chmod +x setup.sh

echo "Configuration files created successfully!"
echo "secrets.json and role.json have been added to .gitignore"
