<div align="center">
<img src="https://raw.githubusercontent.com/dawsonbooth/ascii-art/master/logo.png" alt="ascii-art">
</div>

[![](https://img.shields.io/pypi/v/ascii-art-cli.svg?style=flat)](https://pypi.org/pypi/ascii-art-cli/)
[![](https://img.shields.io/pypi/dw/ascii-art-cli.svg?style=flat)](https://pypi.org/pypi/ascii-art-cli/)
[![](https://img.shields.io/pypi/pyversions/ascii-art-cli.svg?style=flat)](https://pypi.org/pypi/ascii-art-cli/)
[![](https://img.shields.io/pypi/format/ascii-art-cli.svg?style=flat)](https://pypi.org/pypi/ascii-art-cli/)
[![](https://img.shields.io/pypi/l/ascii-art-cli.svg?style=flat)](https://github.com/dawsonbooth/ascii-art/blob/master/LICENSE)

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
ascii-art [-h] [--width WIDTH] [--height HEIGHT] [--chars CHARS] [--font FONT] [--invert] [--normalize] input
```

Positional arguments:

```txt
  input            Path to image from which ASCII art will be generated
```

Optional arguments:

```txt
  -h, --help       show this help message and exit
  --width WIDTH    Character width of ASCII art
  --height HEIGHT  Character height of ASCII art
  --chars CHARS    String containing characters to be seen in ASCII art
  --font FONT      Font for calculating the character weights
  --invert         Whether the ASCII output color is inverted
  --normalize      Whether the weights of the provided ASCII characters are normalized
```

Example:

```bash
ascii-art examples/images/einstein.jpg --width 100 --height 50 --font "Courier" --invert --normalize
```

```txt
,;+;;+;;;,?;?;;;,,,,,,;,;',,'',;%S;;;%SS%SSSSSSSSSSSSSSSSSSSSSSSSS%%%%%%??%%%%;'S+..    .          .
+;;;?;+;,++;;,,,,,;,,,,,,,,,';+%S,,%S%SS#SSSSSS####S#S##S##SSSSSSS%S%%%%%%%S%SS+'%'.                
?+;;,;+;;,;+;;;,,,,;,,,','',;%%%',S%S%SSSSSS#SSSS#SSSSS####SSS#SSSSS%S%%S%%%%S%%%;;'.            .. 
%+;%+;?++;;,,;,,,,,,',,',,;+,%?;'?;%SSSSS#SSSSS##SS######@##SSSS#SSSS%S%S%%%%%S%%'%''        .... . 
?????;;??;;;+,,+,,,,''',;+;;;;;',%%%SSS#######S###########SSS##SSSSSSS%SS%%%%SSS%?',;,   .    ...   
?+;??++;;+;;;,,,,,''',,;%?%%,,''%,%SSSS#######S#####@#######SSS%#SSSSSS%%%%%%SSSS%;?.'''.          .
;?%;;;+;;+;,,,,,,''',;S?;,',;,'+,S%?%SSS#@###SS########@#SSSS#SSSSSSSS%SS%%%%S%S%S?%'  .'    .      
???;;;++,;+;,;',''',%S'?;,+,,?.;?%S%%SSS#@############S###SSSSSSSSSSSSSSSS%%SSSSS%+,,.. ',    .     
??+?;;%++;;,,,,,,;';%',,;;;';%';%'.',+,SSS###SSS##SSS%,',SS%S#%SSSSSSSSSSS%SS%SS%%%,;,.  .'         
%;+;?+;+;;;+,,,,,''?''?;?+,;%?.''.'',%SS##S#SSS##SSSSSS?;,;%??SSSSSSSSSSSSSSSSSSS%?%;'+'..'.        
S????;;;;;;;;;,'',,%,;+,%?,,%;'%;;%%%%SSS##@SSS##SS###SSSSSSSSSSSSS%SSSSSS%SSSSSS%?+;,''.'.'        
?,?+;;?;;;,,;,,,'+,''.%%;,,?%+.;?SSSSS%SSS#S#@###@####S##SSSSSSSS%SSSSSSSSSSSSS%%%????'',. .'..    .
,S;,;;??;;;;,',,''',.,,%;'';%,.%%SS%%%S%%SS####@@#SS#SS#SSSS#SSSSSSSSSSSSSS%SSS%%%%,;?;+.,   .      
%%?;;+%;;;+,,,',.,...,;;,',;?',%SS%%%??SS?%S#@@###SSSS%%+,;%SS#SSS%SSSSSSSSSSSSSSS%%,,+?;,,.   .    
S?%;+;+;,,,,,';'.'.'',%,,,'+%''?S%,,?+?S%%,?S#@#S#SSSSS?+%%%+%SSSS%SSSSSSSSSSSSSSS%%%;?;%%' .       
S,+,;;;+,,,,''......',%''',;?',%?,'##;,?;S?'S@##SSS%%%;';.,S%%SSSS%SSSSS%SSSSSSSSS%S?;%;%;,S.      .
%%?;+,;,;,''.'......''%',',%,';%%'+S...;#%%'S#SSS%SS%?#S...,?%%SSS%SSS%S%SSSSSSSS%+%%?;;%%;,';      
,+?;;,;,,''''.... ..',?,'''%'';%S,;%,'%%;%,%SSSSS%#S%SSS...S%SSSSSSSSSS%SSSSSSS%S%%%??%?;+;;..,.    
,%';,,;,''''......';.';.',.;'';%,;''%?S;SS'%SSSSS%SS%%%?%%%?+%SSSSSSSSS%%%SSSS%%%%%?%;?%%;,++  ;    
%%',';;,',''....'.., ;%.''.;.,+,?%?,%%%%%,,%SSSSSSSS?%S%%%%%%%S%%SSS%SSS%%SSSS%%%%%%%%%,%;;,;;      
S%',,'.;''''...,.....;,'''.'.,%;%%%%%%%%?';SSS%SSSSSSS%%SSSSSS%%SSSS%SS%%%%S%%%%;;;%%%%%+S?'+,' '   
%;..''''','....'....,.,'.'...?%%%SSSS%SS''%SS%%%SSSS#SS#SSSSSSSS%%S%%%S%%%%%%%??S%',+%%%%?%+'+.. .  
%,. ...''.''...'...;'',..S...,%SSSSSSSS%'%SSSS%?%SSS###SSSSSSSSSSSSS%%%%%%%%%%;%%S;%;;%%%%%%%?,. '  
+'  ....''......'.?,''...,...%S#SS?SSS%,+SSSS%%%%SS#SS#S@#SSSS##SSS%%%%%%++;%?%SS%;?;.%%SSS%%?;''.. 
?.  .  .........'.''.....'...%SSSS%SS%S,SS##SSS%?%S##SS########SSSSS%%%%%+;%;SSSSSS.%%%%SSS%;%%',.  
,. ... ........'... ...'''...;#SS%SS%#';SS##@SS%%%%SS@@#S####S##SSS%%+%%?;,%%SSSS%%S%S.%SSSS%%S+'.  
.... .. . .........'..'...'..+%S%%%S#S,,%S#@#SS%SS%%SS@#####S##SS#SS?;%%%;;%S#SSS%SS%S%;SSSS%?S%' . 
?, ....  .... ....'.......,..;?%%SS##',',SSSSS%SSSS?S#S##@#S#S#SSSSS%;%%?%++%%%SS%%SS%%;S#SS,%S%;.'.
,,.... . ..  .. .........,,..++;%S##SS?'.;%%%;#S@%%%SSSS####SSSSS+SS%?%%?%;%S#%S%S%SS%%+SSSS;;S%?.  
%;.. ....   .. ... ..%'+S''..+%;SSSS%%?SSSS#SS#%S%SSSS#S%S#SSSSSSSSS+?%+%%;SSS%S;SSS%S;S#SSS?+S;''. 
;,  %#... .S.  ..... .. '''..%S;%SSSSSSS#S#S%SS#SSSS%SSSSSSSSSSSSSSS%%%%%%,SSS?;??%S%%%SSSSS,,%, '..
',   .........  ... .  .,''..%S;S%S%SS@@SSSS%S##S#S#SSSSSSSSSSSSSSSS+%%?%?+SSS%,%%%?%+SS%S%%,%; ' ..
,' .   . .  ....... .....'...;S,%,?SS%S#%S#SS#SSSS##%SSSSS+SSSSSSSS%;%%%%+%SS%??.'S%%%%;;SS%,'......
'   ...#.  .. .  .. .....'...,%;%?;;%%%SS#SSSS%S#%%%S%SSSSSSSSSSSSS%,S%%%;.S%?' ..;S;,%.'%,. .......
'  . . ......  .... .........'%;%%?,',,?;%;%++S%,,%,?S%#SS%SSSSSSSS%?%S%%%'        .'.  .;'.........
.  ..  . ...   ...............%%%SS;,.'.,'?';,,+SS,'+,;'SSSSSSSSSSS%;SS%+,'            . ...........
   ..   ..  ....... ..........%%'SSS%,,,?;%%?%%%%%;%,..;;SSS#SSSSSS%,SS%+'        .   . ......'....'
        . ..... ...............+%;SSS?.%S%%S%S%%%%%?''++%%?SSSSSSSS?SS%,           . ... .....'..',,
     .    . .  .......'........%S,SS#%.%%%%%%%S%S%?,,%SS#%?SS%SSSSS,S%,         .. ..... .......'',,
         .......................%S?##S.S#%S%S%%;SS;%%%%SSS%SS%SSSS+SS.              ... ....'. ''+,'
       . . ... ........'........'S+S#S.;SS%%;%%+#,,+?%S#SS%S%%SSSS%S  .       .   ...  .......',+,';
            ..'..................;SS#S.+S#SS%;;%S;,,%SSS#SSS?S#S%,%.       .   . .... ..... .,'+,,',
          ',,''''..........'......S'#S.'%@S%%?;%%';%S%SSSSSS;SS%+. .  .  .  .   .  .. . ....,,;,';,,
      . ,,,,,,','............'....'SSS,.%SS+%%%S;%S%SS##SS#SS#S?...      .. .  .... ..... ',;,,';,',
      ,,,',,,,,'''..........'''....%,SS.;%S%%?S%;%SS#S###SS%SS'..   ..   . .  . .   .   .'',++,;,;;,
    ,,,,,,,,,,,',.'.........''''....'?S%.?%?S%?,SS#SSS###SSSS....  ...   .. ..... .. ...';+%?,;,'','
. ,,,;,,,,,,,,,,,'''...''''''''''.....?S..%%%%%S##SSSS#S#S%........     .  .......   ..,,,,',;,;'''.
',,,,,,,,,,',,,,,','....'''''''''......%%..;+;SS@S#SSSSSS,.................... ...   ''',,,',;;+',..
,,,,,;,,,,,',,;,,,'''.''.'''''''''......%%+,%####S####S%............ ...........   .'',;;;'+,;';''..
,;,,,;,,,,,,;,,,;,,''.'''''''''..''......?%SSSSSS#SSS%............ ....'........  ..,,,,',,%;,'''..'
```

By default, the command will output the generated ASCII art to the console. If instead you would like to output to a file, feel free to use the redirection `>` operator. More info on that [here](https://linuxcommand.org/lc3_lts0070.php).

Feel free to [check out the docs](https://dawsonbooth.github.io/ascii-art/) for more information on how to use this package.

# License

This software is released under the terms of [MIT license](LICENSE).
