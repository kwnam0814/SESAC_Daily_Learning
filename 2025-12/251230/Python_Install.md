\# Python 설치

\## pyenv

\- 한 대의 컴퓨터에서 여러 버전의 파이썬을 자유롭게 설치하고 전환할 수 있게 해주는 파이썬 버전 관리 도구

\### Windows ver.



\#### pyenv 설치



1\. windows 키 -> PowerShell 검색 -> 관리자 권한으로 실행



2\. 아래 명령어 입력 후 PowerShell 종료

```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force```



3\. PowerShell 관리자 권한으로 실행 후 아래 명령어 입력

```git clone https://github.com/pyenv-win/pyenv-win.git "$env:USERPROFILE\\.pyenv"```

```\[System.Environment]::SetEnvironmentVariable('PYENV', $env:USERPROFILE + "\\.pyenv\\pyenv-win\\", "User")```

```\[System.Environment]::SetEnvironmentVariable('PYENV\_ROOT', $env:USERPROFILE + "\\.pyenv\\pyenv-win\\", "User")```

```\[System.Environment]::SetEnvironmentVariable('PYENV\_HOME', $env:USERPROFILE + "\\.pyenv\\pyenv-win\\", "User")```

```\[System.Environment]::SetEnvironmentVariable('PATH', $env:USERPROFILE + "\\.pyenv\\pyenv-win\\bin;" + $env:USERPROFILE + "\\.pyenv\\pyenv-win\\shims;" + \[System.Environment]::GetEnvironmentVariable('PATH', "User"), "User")```



\#### Python 설치

1\. Python 3.12 ver. 설치

&nbsp;   - PowerShell 에 다음 명령어 입력 ```pyenv install 3.12```

2\. 3.12 ver. Python 설정

&nbsp;   - PowerShell 에 다음 명령어 입력 ```pyenv global 3.12```

3\. Python ver. 확인 ```python --version```



\### MacOS ver.

\#### pyenv 설치

1\. Terminal 열기

2\. 아래 명령어 실행

```brew install pyenv```

```echo 'export PYENV\_ROOT="$HOME/.pyenv"' >> ~/.zshrc```

```echo '\[\[ -d $PYENV\_ROOT/bin ]] \&\& export PATH="$PYENV\_ROOT/bin:$PATH"' >> ~/.zshrc```

```echo 'eval "$(pyenv init -)"' >> ~/.zshrc```



\#### Python 설치

1\. 파이썬 3.12 ver. 설치

&nbsp;   - Terminal 에 다음 명령어 입력 ```pyenv install 3.12```

2\. 3.12 ver. 의 Python 설정

&nbsp;   - Terminal 에 다음 명령어 입력 ```pyenv global 3.12```

3\. Python ver. 확인 ```python --version```

