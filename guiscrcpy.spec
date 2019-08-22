# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/media/ss/WD-SS/Srevin/Python/guiscrcpy'],
             binaries=[],
             datas=[('ui/android_circle.png', 'ui'), ('rsrc/monitor.png', 'rsrc'), ('rsrc/clip.png', 'rsrc'), ('rsrc/potrait.png', 'rsrc'), ('rsrc/landscape.png', 'rsrc'), ('rsrc/credit-card.png', 'rsrc'), ('rsrc/bell.png', 'rsrc'), ('rsrc/layout.png', 'rsrc'), ('rsrc/volume.png', 'rsrc'), ('rsrc/power.png', 'rsrc'), ('rsrc/menu.png', 'rsrc'), ('rsrc/home.png', 'rsrc'), ('rsrc/left-arrow-1.png', 'rsrc'), ('rsrc/lightning.png', 'rsrc'), ('rsrc/cancel-1.png', 'rsrc')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['web', 'audio'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='guiscrcpy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='guiscrcpy')
