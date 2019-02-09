# SyncFilenameBySize

* https://www.clien.net/service/board/cm_linux/13126944 의 글타래에서 논의된 스크립트을 파이썬으로 구현하였습니다.
* 두 디렉토리의 파일 용량을 비교하여 파일명을 동기화합니다.

## Usage
* python syncfilename.py 대상디렉토리 목표디렉토리

## Feature
* 대상디렉토리에 있는 파일들의 크기을 이용하여 목표디렉토리의 파일명을 변경합니다.
* 파일크기는 바이트 단위로 계산합니다.
* 대상디렉토리에 같은 크기의 파일이 있다면 실행이 중지되고 에러가 출력됩니다.
* 작업은 취소할 수 없습니다.
* Python 2.7 / 3.6 에서 테스트 되었습니다.
* 윈도우10과 CentOS 7에서 테스트 되었습니다.

## Screenshot
![결과화면](https://github.com/dongbum/SyncFilenameBySize/blob/master/images/result.png "결과화면")
