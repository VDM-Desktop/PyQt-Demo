# PyQt Demo for Reentrant Application Framework (RAF)

### Module Structure
- `channel`: channel descriptions between `descriptors`
    - **intra-process**: use shared memory space in stack;
    - **inter-process**: use dual `multiprocessing.Queue`;
    - **inter-remote**: use dual UDP sockets;
- `descriptor`: atomic element of PyRAF program
    - **DeviceDescriptor**: maintain the global I/O devices mapping, e.g., tty, keyboard/mouse, etc.
    - **FileDescriptor**: maintain a pseudo file system with all remote devices;
    - **SocketDescriptor**: maintain all network connections over a virtual network interface;
- `remote`: IP-based remote devices management
    - discovery, offloading, daemon, and etc.

### Notes
1. PyRAF is not a P2P framework, the APP is hosted by the device with the `Yggdrasil`;
2. `Yggdrasil` is composed of `ChannelDescriptor`s (as truss) and other `BaseDescriptor`s (assembled on truss);
3. PyRAF enables a high-level garbage collection. The retain/resume design will drain the memory leak of the descriptors;