DISK_NAME=windows.img
if [ ! -f "./disk/$DISK_NAME" ]; then
    echo "disk file not exsit install ing system pls wait";
    cp -p raw/$DISK_NAME disk/$DISK_NAME
fi
qemu-system-x86_64 -m $(free -g | grep Mem | awk '{print $2}')G -drive file=disk/$DISK_NAME,format=qcow2 -boot b -enable-kvm -cpu host -smp $(nproc) -full-screen -vga virtio -display sdl

