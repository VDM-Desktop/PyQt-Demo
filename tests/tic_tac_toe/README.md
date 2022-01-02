
### Descriptions
该应用实现分布式的井字棋游戏，包含两个棋盘，共享状态；
两个棋盘可以在同一进程、不同进程 或 不同机器上启动。

1. desc都在本机同一进程中启动，A和B可操作并符合游戏逻辑；
2. 通过console将棋盘B停下，再启动棋盘B，B窗口位置和大小不变，A和B保持状态同步；
3. 通过console将棋盘B停下并在新进程中启动，A和B保持状态同步；
4. 通过console将棋盘B停下并offload到局域网中另一机器，A和B保持状态同步。

### Descriptors and Instances
- **PlayerBoard**: `BaseDescriptor`, `QWidget`
    ```python
    player_x = PlayerBoard('X')
    player_o = PlayerBoard('O')
    ```
- **Console**: `BaseDescriptor`
    ```python
    console = Console()
    ```

### Channel Descriptors
```python
pyraf.connect(player_x, player_o, 'shared')
```
