# A PyQt Demo for Reentrant Application Framework (RAF)

The concept of RAF is proposed to demonstrate the possibility of developing interruptible applications.
A RAF application is loosely decoupled into multiple **descriptors** with **channels** to maintain the data stream. The structure could be described via Directed *Cyclic* Graph.
Each descriptor could run on different devices connected via wireguard

### The Design

Each descriptor should implement the `retain/restore` primitives to maintain its own state, e.g., I/O devices, file system, graphics buffer, network connection, etc.

The channel is also implemented as a descriptor which is responsible to share data between the descriptors.
The design of channel model is multi-fold.

**Subscriptions**:
- *shared* (default): on-demand uni/bi-direction
- *propagate*: best-effort uni/bi-direction
- *tether*: real-time bi-direction
- *stream*: uni-direction with sampling frequency

**Efficiency**:
- *intra-process* channel should use shared memory space in stack;
- *inter-process* channel may use dual `multiprocessing.Queue`;
- *inter-remote* channel may use dual UDP sockets.

**Reliability**:
- *fec*: FEC-encoded correction
- *lossy*: lossy compression for multimedia buffer

### Notes
1. PyRAF is not a P2P framework, the APP is hosted by the device with the `Yggdrasil`;
2. `Yggdrasil` is composed of `ChannelDescriptor`s (as truss) and other `BaseDescriptor`s (assembled on truss);
3. PyRAF enables a high-level garbage collection. The `retain/restore` cycle can drain the memory leak of the descriptors at the cost of memory overhead.

<!-- ### Module Structure
- `channel`: channel descriptions between `descriptors`
    - **intra-process**: use shared memory space in stack;
    - **inter-process**: use dual `multiprocessing.Queue`;
    - **inter-remote**: use dual UDP sockets;
- `descriptor`: atomic element of PyRAF program
    - **DeviceDescriptor**: maintain the global I/O devices mapping, e.g., tty, keyboard/mouse, etc.
    - **FileDescriptor**: maintain a pseudo file system with all remote devices;
    - **SocketDescriptor**: maintain all network connections over a virtual network interface;
- `remote`: IP-based remote devices management
    - discovery, offloading, daemon, and etc. -->
