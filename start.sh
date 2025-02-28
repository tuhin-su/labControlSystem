#!/bin/bash

# Trap Ctrl+C and other signals to disable exit
# trap "echo 'Exit is disabled!';" SIGINT SIGTERM SIGQUIT

# Function to check for updates
check_updates() {
    git fetch -a
    LOCAL=$(git rev-parse HEAD)
    REMOTE=$(git rev-parse origin/$(git symbolic-ref --short HEAD))
    if [ "$LOCAL" != "$REMOTE" ]; then
        echo "Updates are available, pulling them..."
        git pull origin $(git symbolic-ref --short HEAD)
    else
        echo "No updates available."
    fi
}

start_windows() {
    echo "Starting the Windows... pls wait."
    bash -c "./start_windows.sh"
}

# Function to stop (exit the script)
stop_windows() {
    echo "Wepping all data pls wait"
    bash -c "./erase_windows.sh"
}

start_linux() {
    echo "Starting the update process for Linux..."
    bash -c "./start_linux.sh"
}

# Function to stop (exit the script)
stop_linux() {
    echo "Stopping the script. No action taken."
    echo "Wepping all data pls wait"
    bash -c "./erase_linux.sh"
}

menu() {
    # check_updates
    echo "Please choose an option:"
    echo "1. Boot in Windows"
    echo "2. Boot in Linux"
    echo "3. Factory Reset Windows"
    echo "4. Factory Reset Linux"
    read -p "Enter 1, 2, 3 or 4: " choice

    case $choice in
        1)
            start_windows
            ;;
        2)
            start_linux
            ;;
        3)
            stop_windows
            ;;
        4)
            stop_linux
            ;;
        *)
            echo "Invalid choice! Please enter 1, 2, 3, or 4."
            menu
            ;;
    esac
}

menu
