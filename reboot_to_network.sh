#!/bin/bash

# Check if the system is using UEFI (only applicable to UEFI systems)
if [ -d /sys/firmware/efi ]; then
    # Get the boot entry number for the network boot entry (find the one with "Network Boot")
    NETWORK_BOOT_ENTRY=$(sudo efibootmgr | grep -i 'Network Boot' | awk '{print $1}' | cut -d' ' -f2)

    if [ -z "$NETWORK_BOOT_ENTRY" ]; then
        echo "Network Boot entry not found!"
        exit 1
    fi

    # Set network boot as the first boot option
    echo "Setting network boot as the first boot option..."
    sudo efibootmgr -o $NETWORK_BOOT_ENTRY,0,1,2,3,4,5

    # Reboot the system into PXE boot
    echo "Rebooting into network boot mode..."
    sudo reboot
else
    echo "This system is not using UEFI. Cannot modify boot order for PXE boot."
    exit 1
fi
