pyinstaller 是一个命令行工具，用于将 Python 程序打包成独立的可执行文件。下面是该工具支持的选项及其解释：

位置参数 (Positional Arguments):

scriptname：要处理的脚本文件名称，或者是一个 .spec 文件的名称。如果指定了 .spec 文件，那么大多数选项都将是多余的，并会被忽略。

选项 (Options):

-h, --help：显示帮助信息并退出。

-v, --version：显示程序版本信息并退出。

--distpath DIR：指定打包后的应用程序存放的目录（默认是 ./dist）。

--workpath WORKPATH：指定所有临时工作文件（如 .log, .pyz 等）存放的目录（默认是 ./build）。

-y, --noconfirm：在执行过程中不提示任何确认信息，例如覆盖文件等。

--add-data SOURCE:DEST：添加非二进制文件到生成的可执行文件中。SOURCE 是源文件路径，DEST 是目标路径。

--add-binary SOURCE:DEST：添加二进制文件到生成的可执行文件中。SOURCE 是源文件路径，DEST 是目标路径。

-p DIR：为 Python 导入添加搜索路径。

--hidden-import MODULENAME：强制导入一个模块，即使它似乎不被自动检测到。

--collect-submodules MODULENAME：收集指定模块的所有子模块。

--collect-data MODULENAME：收集指定模块的所有非代码文件。

--collect-binaries MODULENAME：收集指定模块的所有二进制文件。

--collect-all MODULENAME：收集指定模块的所有数据（包括子模块、非代码文件和二进制文件）。

--copy-metadata PACKAGENAME：复制指定包的元数据。

--recursive-copy-metadata PACKAGENAME：递归地复制指定包及其所有子包的元数据。

--additional-hooks-dir HOOKSPATH：指定额外的钩子脚本的目录。

--runtime-hook RUNTIME_HOOKS：指定运行时钩子脚本。

--exclude-module EXCLUDES：排除指定的模块。

--splash IMAGE_FILE：设置启动画面为指定的图像文件。

-d {all,imports,bootloader,noarchive}：设置调试模式。可以指定 all、imports、bootloader 或 noarchive。

--python-option PYTHON_OPTION：设置 Python 解释器的选项。

-s：在生成的可执行文件中不包含控制台窗口（仅适用于 Windows）。

--noupx：不使用 UPX 进行压缩（UPX 是一个可执行文件压缩工具）。

--upx-exclude FILE：排除指定的文件不使用 UPX 进行压缩。

-c：生成的控制台应用程序在关闭时不会退出系统。

-w：在生成的可执行文件中不包含控制台窗口（仅适用于 Windows）。

--hide-console {minimize-late,minimize-early,hide-late,hide-early}：控制控制台窗口的显示和隐藏行为。

-i <FILE.ico or FILE.exe,ID or FILE.icns or Image or "NONE">：设置生成的可执行文件的图标。

--disable-windowed-traceback：禁用窗口化的 traceback（错误跟踪信息）。

--version-file FILE：指定版本信息文件的路径。

-m <FILE or XML>：指定元数据文件或 XML 文件的路径。

-r RESOURCE：指定要添加到可执行文件中的资源文件。

--uac-admin：要求以管理员权限运行生成的应用程序（仅适用于 Windows）。

--uac-uiaccess：允许辅助技术（如屏幕阅读器）与生成的应用程序进行交互（仅适用于 Windows）。

--argv-emulation：模拟命令行参数传递。

--osx-bundle-identifier BUNDLE_IDENTIFIER：设置 macOS 应用程序的 bundle 标识符。

--target-architecture ARCH：指定目标架构。

--codesign-identity IDENTITY：指定代码签名身份（仅适用于 macOS）。

--osx-entitlements-file FILENAME：指定 macOS 应用程序的权限文件。

--runtime-tmpdir PATH：设置运行时临时目录的路径。

--bootloader-ignore-signals：使引导加载程序忽略信号。

--distpath DIR：指定打包后的应用程序存放的目录（与之前的选项重复，可能是个错误）。

`--workpath