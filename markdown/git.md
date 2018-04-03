# GIT이란 무엇인가?  
**Git**이란 분산 버전관리 시스템의 대표 프로그램 중 하나이다.   
간단히 설명해서 나의 local repository / Remote repository / 다른 협력자의 repository등 여러 repository에서 블록체인 기술과 비슷하게 각각 repository에 해당 프로젝트르 저장함으로써 안정성을 높인 버전관리 서비스이다.   

### GIT 핵심명령어 

*git init* - 현재 경로의 디렉토리에 .git 파일을 추가하여 버전관리시스템을 사용할수 있게 한다.  
*git status* - 현재 깃의 상태를 보여준다. 추적되는 파일이나 추적되지않는 파일, 변경되었으나 깃에 커밋되지않은 파일등을 보여준다.  
*git add* 파일명 or 디렉토리명 - 깃이 특정 파일을 추적하게 해준다. 디렉토리를 추적하게하면 그 하위파일도 모두 추적한다. 현재 파일의 스냅샷을 찍어 staged 상태로 넣어주는 명령이다. 
*git commit* 나의 local repository에 커밋을 하는 명령어이다. 옵션없이 이렇게만 명령어를 치면 문서가 뜨게되며 그 안에 커밋내용을 적어야 한다. 귀찮으면 -m "커밋" 이런식으로 간단하게 쓸수 있다.
*git commit --amend* 이전 commit을 덮어쓴다. 
*git push* 나의 local repository에 있는 버전을 remote repository로 푸시하는 명령어이다. 
*git clone* 반대로 remote repository에서 나의 local repository로 현재 버전을 가져오는 명령어이다.    
*git reset 파일명* git add로 잘못 넣은 파일을 다시 unstaged 상태로 만들수있다. 
*git branch* branch를 만든다. 이 명령어는 branch를 생성하기만 할뿐 그 branch로 옮기지는 않는다. 
*git checkout* 해당 branch로 이동한다. 

#### 기타내용
.gitignore - 이 파일과 이 파일 안에 써있는 파일들을 커밋할때 무시하게한다.   
Working tree - git init 했을때의 현재 폴더
git add를 하면 파일을 추적하게 하고, 그 명령어를 칠때의 파일의 스냅샷을 기억한다. (staged 상태) 이렇게 몇개의 파일을 add하여 추적하게하고, 스냅샷을 기억하게 한후 
git commit을 하면 add된 파일(staged된 파일)들의 스냅샷을 local repository에 저장한다.
여기서 git push를 하면 remote repository에 내 local repository에 commit했던 것이 저장된다. 
