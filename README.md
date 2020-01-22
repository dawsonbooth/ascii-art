[![](https://img.shields.io/pypi/v/ascii-art-cli.svg?style=flat)](https://pypi.org/pypi/ascii-art-cli/)
[![](https://img.shields.io/pypi/dw/ascii-art-cli.svg?style=flat)](https://pypi.org/pypi/ascii-art-cli/)
[![](https://img.shields.io/pypi/pyversions/ascii-art-cli.svg?style=flat)](https://pypi.org/pypi/ascii-art-cli/)
[![](https://img.shields.io/pypi/format/ascii-art-cli.svg?style=flat)](https://pypi.org/pypi/ascii-art-cli/)
[![](https://img.shields.io/pypi/l/ascii-art-cli.svg?style=flat)](https://github.com/dawsonbooth/ascii-art/blob/master/LICENSE)

![](https://raw.githubusercontent.com/dawsonbooth/ascii-art/master/logo.png)

# Description

Named as such, this package is a command-line ASCII art generator written in Python. There is a variety of customization parameters which are detailed below.

# Installation

With Python installed, install the package from PyPI with the following command:

```bash
pip install ascii-art-cli
```

This package is not to be confused with [ascii_art](https://pypi.org/project/ascii_art/) or other various ASCII art packages.

# Usage

This is a command-line program, and can be executed as follows:

```bash
ascii-art [-h] [--output OUTPUT] [--width WIDTH] [--height HEIGHT] [--chars CHARS] [--font FONT] [--invert] [--normalize] [--terminal] input
```

Positional arguments:

```
input: Path to image from which ASCII art will be generated
```

Optional arguments:

```
  -h, --help        Show the help message and exit
  --output OUTPUT   Path to output generated ASCII art
  --width WIDTH     Character width of ASCII art
  --height HEIGHT   Character height of ASCII art
  --chars CHARS     Path to characters to be seen in ASCII art
  --font FONT       Font for calculating the character weights
  --invert          Whether the ASCII output color is inverted
  --normalize       Whether the weights of the provided ASCII characters are normalized
  --terminal        Whether to output to the terminal
```

Example:

```bash
ascii-art examples/images/einstein.jpg --width 100 --height 50 --font "Courier" --terminal --normalize
```

```
%%++%+++%%;+;%%+%%%%%S%%+SSSSSS+,'%++;'','''.''''.'''.'.''''.''''',,,,,,;;,,,'%S'+##@@@@#@@@@@@@@@@#
+++%;%+%%++%+SS%S%+%S%%SS%S%S%+,'S%;','....''... .............'.'',',,,;,;,',''+S,S#@@@@@@@@@@@@@@@@
;++%S%++%%++%++%%%%%%SSSSSS%%;,,SS',',..........................''.''';'',,,,',,;%%##@@@@@@@@@@@@##@
;++;++;++%%%%+S%%%SSSSSSSS%+%,;%S;+,..''............ ...   ...''..''.,',',;,,,'',S,SS@@@@@@@@####@#@
;;;;;%+;;+%%+S%+SSSSSSSS++%++%+SS,,;''.. . .... ....     ...'..'''.''','',,,,''',;#S%S@@@#@@@@###@@@
;++;;++%%+++%%%%SSSSSSS+;;,;S%SS,%,''....... ... ..   ..  . ..''.'''.'',,',,,'''',%;###S#@@@@@@@@@@#
+;,+%++%++%S%SSSSSSS%%.;%SS%+SS+%',;,'... .. ....... ..  ...'...'''''','',,,'',',';,#@@#S@@@@#@@@@@@
;;;%%+++%%+%%%SSSSS%,'S;%%+SS;#+;,'',....  . ... ... ............''''.'''',,'..'',+S%##@#S@@@@#@@@@@
;;+;+%;++%%%%SSSS%S%;S%S%++S+,#+,S##S+%'............',SS%'',..,..'''''.'''''''.',,'%+%#@@#S@@@@@@@@@
,+++;+%++%++%%SSSSS;S#;+;+%%;;#SS##SS,''. ........'.''.;%%%,;;.''.'''''''''''.''';;,%S+S####@@@@@@@@
.;;;;++++%++++SSS%%,S%+S,;SS,%#,%+,',,'''.. .... ... ..'.'..'.....',''.''',''.''';;++SSS###S@@@@@@@@
;%;+%+;%++%%%S%%S+%SS#,;+SS;,+#+;''''''......  .  ..............','''..'''''.'.';,;;;;SSS#@####@@@@#
S.+%%%;;%%%+%SSSSS#S#SS,+SS+;%#,''.,,,',,'...     .'.............'''''''''','.',,,;S+;%+#S@@@#@@@@@@
,,;%++;%%%+SSSSS#S###S+%%S%%;SS,.';;;;;'';,.    .....',;+S%,'....','..'''''....''',,%%+;%SS#@@@#@@@@
';,++%+%%%S%SS%##S#SSS;SSSS+,#S;';%S;+;.''%;..  ....'.';+,,,+,...',''''.'''.'...'',,;+;%,,S@#@@@@@@@
.%+%++%+%SSSSS#######S,SSSS%;#S;;S#. %%;+';S.  ...',';+S%#%',,'''','..'';.'''..''',';+;+;%%'#@@@@@@#
,,;++%%%%SSS########SS,SSSS,%#%,'S+.###%.,,S.....,'',;..###S;',...,''',',''''..'''+,,;+%,,%S#%@@@@@@
S+;+%S%%%SSS#####@##SS;SSSS,#S%,'%+,%S,,%,S,'...', ','''###.;''''.'''.''''''''',',,,;;;;+++%##S#@@@@
%,S+%%%SSSSS######S+#S%#SS#+#S%,S%SS;;'%.'S,...'''.',,;;,,';+,'''.''''',,,'''',;;,;;,+;,;+S++@@%@@@@
',SSS%+S#SSS####S##S@+,##S#+#S+%;,;%;,',;SS;.''''.'';,'',,,,,,',,..''.'''''.'',;,,,,;,;S,+%S+%@@@@@@
',SSSS#%SSS####S#####%S##S###%;%;,,,,,,,;S+.'.,'.'...',,'''.'',,'..','',,,,',,,,++%;,',,+';S+SS@S@@@
,%##SS#S#S#####S####%#SS#S###;;','.'',..SS,'.,,'''......'.'''''',''',,',,,,,;,;;',SS+',,,;,+S+##@#@@
;S#@###SS##########+#SS##'###%,''''..'.,S;'''',;,.'.. .....'.'...'.',,,,,,,',,%;''%,%%;;,;,;;;%#@#@@
+S@@####SS######S#;SSS###%###;'...;...,%+.''',,,,'..'... ..........,,,,;,+++';;'.,+;%#,,''',,;+####@
;#@@#@@#########S#S######S###;'..','','S'.....',;,'. ...... .. ...'';,;,,+%,+''..''#,,;,''',%,,S%#@@
S#@###@############@####SS###+.''''''.S%'.   ..,',,'.  .. ........',,+;,;+%,,..'.,,.,.#,..'',;'+S#@@
####@##@#@############S###S##+,''''..'%S,.  ..'''.,,'.    . ......'';%,,,%%,'....'..'.;%...',;',S@#@
;%@####@@####@####S#######S##%;,;'. .S%SS'..'','..';'.'    .......'',%,,;;++;,,.';,..',+...'%;',%#S#
S%####@#@##@@##@#########%S##+++,'..'';S#+,,,%.. ,,,...'..  ..'..+'',;,,;;%,..,',','.',+..'.++';;#@@
,+##@####@@@##@###@##,S+'SS##+,%'..',,;'''' .'.'''......'........'''+;,+,,+...,'%''.,'+...'.;+'%SS#@
%S@@, ###@#'#@@#####@##@#####,'%,''''''.....'.. '..',..'''...'.'...',,,,;,S'..;+;;;',,,..''.S%,%@###
S%@@@#########@@###@#@@#SSS##,'+',.,..  .'..,...'...'.''''....''..''+,,;,;+''';S;,;;;+'',',,%,%@S@##
%S@#@@@#@#@@#######@#####S###%'%,%;.',' '.... .''...,.''''+..'....',+,,,,+,.'';;##'',,'%%'.;%#######
#@@@###.#@@##@#@@##@#########S;%,;+%,,,'' .''.,..,,,','.'.'..'....',%',,,%#',;#@##%'+%;#S,S#@#######
S@@#@#@######@@####@#########S,+',;%#S%;%,%,++',SS,S;',.'.'.'.....',;,',;;S@@@@@@@@#S#@@#%S#########
#@@##@@#@###@@@###############,;;''%S#S#%#;S%%%+''%S+S+#..''..'.'.',%'',+%S@@@@@@@@@@@@#@###########
@@@##@@@##@@#######@##########;'S'..,SSS;%;,;,,,',%;%##%%'.'..'...';%.';+S@@@@@@@@#@@@#@###########S
@@@@@@@@#@#####@###############+,+..';#,.;,';',',,,;S#++',;..'....';'''%@@@@@@@@@@@#@###@#####S##S%%
@@@@@#@@@@#@#@@################;'%'..,#',,,,,;';',;SS,'..';.','...'%',%@@@@@@@@@##@#####@#######SS%S
@@@@@@@@@#######################,';. '#' ,';',,+'.%,;,,...,'',....+''#@@@@@@@@@@@@@@###@######@S#+%S
@@@@@@@#@#@###@#################S'+...#+'',,%,,+.%S+;,'..','',...',.@@#@@@@@@@#@@@###@@#######SS+SS+
@@@@@@@@@@@@#####################+'' '#+'.'.'%%,'%S%;.....'.;...,S'#@@@@@@@#@@@#@####@#####@#SS+S%SS
@@@@@@@@@@SSSSSS##################'S.'##, '',;+',S+,',....'.%..'+#@#@@#@@#@@#@@@#@@##@#@####%%+SS%SS
@@@@@@#@SSS%SSSS#############S####S'''%#,'.+,,,'%,','......'...;###@@@@@@##@#@@####@#####@SS%SSS+SSS
@@@@@@SS%SSSS%SSSS#################,S''#%'.,,;';+,'.... ...;.'S##@@@##@@@#@#@@#@#@@@#@@@#SS%++S+S%+S
@@@@%%SSS%S%S%SSS###################S;',#;,;',;S...''.. ..'''####@@###@@@##@#####@##@###S++;;S%SSSS#
#@%SS%%%S%%SS%S%SSS#######S#SS########;'##,,,,;'.....'...',########@@@@@#@@#######@@@##%%S%S%%S%#S##
SS%S%%%S%%SSS%S%%SSS#####S#S#S#########;'##++%.. ..'....'%####################@###@@@#SSSSSS%%%+SS##
%SS%S%%%%SSS%S%%SSSS######SS##SSS#######,,+S,. ... ....,############@###########@@@#SS%+%%#+%%S+S###
S%%%S+%%%%%%%%%S%%S###SS##SSSS###########;,''........,############@#############@@##S%SSSSS,%SSSS##S
```

# License

This software is released under the terms of [MIT license](LICENSE).
