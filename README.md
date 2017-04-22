# SVD - Simple Video Downloader
### Faça download de vídeos do Youtube e outros websites suportados pelo youtube-dl!

### Descrição:

##### Este programa foi desenvolvido em Python e utiliza o programa youtube-dl para baixar vídeos do youtube e outros sites suportados.
##### Este programa também utiliza o software FFmpeg, que possui a função de converter os vídeos baixados para diversos formatos de áudio e vídeo.
##### Este programa foi compilado utilizando o PyInstaller, portanto não requer que o usuário possua o interpretador Python instalado.

##### Ao executar o programa, será requisitado a URL do vídeo ou da playlist, um formato de áudio/vídeo desejado e a pasta de destino onde será armazenado o arquivo. Ao inserir estas informações, o programa irá se encarregar de baixar os vídeos diretamente do youtube ou de outros sites suportados pelo youtube-dl.

##### Ao apertar o botão "Download", espere o programa terminar de baixar e, se necessário, converter o arquivo. Você saberá quando estará terminado assim que uma janela do explorer abrir na pasta do arquivo de destino e o botão Download estiver disponível novamente.

##### Fique atento ao terminal! É nele que as informações de download estarão sendo mostradas. Caso ocorra algum erro, será informado no terminal.

![SVD - Simple Video Downloader](http://i.imgur.com/FMJTT8x.png)

### Atualizações:

##### As vezes é necessário que o youtube-dl esteja totalmente atualizado para que ele possa funcionar corretamente!

##### Para atualizar o youtube-dl, abra o programa, clique no menu Atualizar e clique na opção youtube-dl. Caso exista uma atualização, o próprio youtube-dl irá se encarregar de fazer o processo de atualização.

##### Caso queira atualizar manualmente, acesse a página de [download do youtube-dl](https://rg3.github.io/youtube-dl/download.html), Baixe a versão "Windows.exe" e cole na pasta /bin deste programa.

### Formatos:

##### Os seguintes formatos de áudio e vídeo estão disponíveis:
- ***Audio:*** mp3, wav.
- ***Video:*** mp4, webm, mkv, 3gp.

##### O programa também oferece opções de baixar os vídeos em seu formato nativo ou por conversão. Caso queira fazer a conversão de um formato de vídeo, utilize a opção (Conversão), ao lado do formato escolhido (exemplo: MP4 (Conversão), WEBM (Conversão), MKV (Conversão)).

##### ***Atenção!*** Para que os formatos de conversão estejam disponíveis nas Opções de Salvamento do programa, é necessário que o programa FFmpeg esteja dentro da pasta /bin, junto ao youtube-dl!

### Requisitos:

#### Compilando:
- Python 2.7
- PyQt4 para Python 2.7
- PyInstaller
- Microsoft Visual C++ 2010 Redistributable (Windows apenas)

##### Para compilar o programa, basta executar o script build.bat (Windows).
##### ***OBS:*** É necessário que o programa pyinstaller seja reconhecido como comando interno no prompt de comando (Windows), caso contrário o script para compilar o programa irá falhar!

#### Binário:
- ***Windows:*** Requer o Microsoft Visual C++ 2010 Redistributable instalado (provavelmente já vem instalado em sistemas atualizados).
##### O programa, em seu formato binário, não requer o Python ou o PyInstaller instalados!

### Download:
#### Windows: https://github.com/Wolfterro/SVD/releases/tag/v1.0-Windows

###### Caso não possua o git e queira também baixar o repositório por completo, baixe através deste [Link](https://github.com/Wolfterro/SVD/archive/master.zip) ou clique em "Clone or Download", no topo da página.
