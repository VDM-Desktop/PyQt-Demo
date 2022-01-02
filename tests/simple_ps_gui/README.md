
### Descriptions
该应用实现一个分布式的类top的进程管理，可以在一个列表里同时列出多台机器的进程（通过远程拉起 Descriptor 来实现）；
包含进程的 机器名、PID、命令行、CPU、MEM、TTY信息。

1. 可以列出本地信息，并实时更新；
2. 异步获取remote列表，动态 start/stop 远程descriptor；
3. 可以列出远程信息，并实时更新。

### Descriptors and Instances
- **MainWindow**: `BaseDescriptor`, `QWidget`
    ```python
    mw = MainWindow()
    ```
- **ProcessDesc**: `BaseDescriptor`
    ```python
    pd = ProcessDesc()
    ```

### Connections
```python
pyraf.connect(pd, mw, 'forward')
# or, `pd >> mw`
```
