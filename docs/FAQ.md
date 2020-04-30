# FAQ

## `Ctrl-C` doesn’t stop the program

Yes, `Ctrl+C` will not stop guiscrcpy. This is because PyQt5’s renderer dos not handle `SIGINT` or `KeyboardInterrupt`. You can use a Task Manager to kill it or use the commanline `kill` / `killall`. If you try to use `Ctrl+C`, it can force guiscrcpy into an unresponsive state, and later hangs. Alternatively, use the close button to stop it.

## `libQt*.so.*` is not found?

This is probably because you have two installations of `PyQt5` or `PySide2`, The `PySide2` and `PyQt5` are conflicting packages. Uninstalling one of them will not fix the error. This is because `pip` uninstalls the co-referenced file, which later becomes missing. The solution, is however to create a [`virtual environment`](https://google/search?q=python+virtual+environment) or to uninstall `PyQt5` (and `PySide2` if it exists) and reinstall them on local level. If the PyQt5 level matches the system level only, you can either uninstall all local level `PyQt5` or you can run `guiscrcpy` with

```bash
python -s $(which guiscrcpy)
```



