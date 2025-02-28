if [ ! -f "raw/linux.img" ]; then
    echo "Systetem croped rebooting recovary mode"
    bash -c "reboot_to_network.sh"
fi
echo "Installing System pls wait it take up to 25 minits"
cp -p raw/linux.img disk/linux.img
