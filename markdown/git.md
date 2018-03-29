#GIT이란 무엇인가?  
**Git**이란 분산 버전관리 시스템의 대표 프로그램 중 하나이다.   
간단히 설명해서 나의 local repository / Remote repository / 다른 협력자의 repository등 여러 repository에서 블록체인 기술과 비슷하게 각각 repository에 해당 프로젝트르 저장함으로써 안정성을 높인 버전관리 서비스이다.   

###GIT 핵심명령어 


*git init* - 현재 경로의 디렉토리에 .git 파일을 추가하여 버전관리시스템을 사용할수 있게 한다.  
*git status* - 현재 깃의 상태를 보여준다. 추적되는 파일이나 추적되지않는 파일, 변경되었으나 깃에 커밋되지않은 파일등을 보여준다.  
*git add* 파일명 or 디렉토리명 - 깃이 특정 파일을 추적하게 해준다. 디렉토리를 추적하게하면 그 하위파일도 모두 추적한다. 현재 파일의 스냅샷을 찍어 staged 상태로 넣어주는 명령이다. 

.gitignore - 이 파일과 이 파일 안에 써있는 파일들을 커밋할때 무시하게한다.   

git init 했을때의 그 폴더가 Working tree,
git add를 하면 파일을 추적하게 하고, 그 명령어를 칠때의 파일의 스냅샷을 기억한다. (staged 상태)
이렇게 몇개의 파일을 add하여 추적하게하고, 스냅샷을 기억하게 한후 
git commit을 하면 add된 파일(staged된 파일)들의 스냅샷을 local repository에 저장한다.
여기서 git push를 하면 remote repository에 내 local repository에 commit했던 것이 저장된다. clone은 remote에서 local로. 