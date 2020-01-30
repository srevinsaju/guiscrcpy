# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['scripts\\guiscrcpy'],
             pathex=['C:\\Users\\SS\\repo\\guiscrcpy'],
             binaries=[],
             datas=[],
             hiddenimports=['guiscrcpy'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='guiscrcpy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='guiscrcpy\\ui\\icons\\guiscrcpy_logo_SRj_icon.ico')
