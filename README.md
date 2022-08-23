# 📌 혼자서도 잘해요리
<img src="https://velog.velcdn.com/images/tasha_han_1234/post/cdea5acf-3f14-492d-a0be-7e5d87c81249/image.png">

- 혼자서도 잘해요리는 1인가구 사용자에게 레시피를 검색, 추천 기능을 제공하는 웹입니다.<br>
- 사용자는 게시된 다양한 레시피를 참조할 수 있습니다.<br>
- 또한 자신이 레시피를 직접 작성하여 다른 사용자와 공유할 수 있습니다.<br>
- 형태소로 분리된 재료들을 바탕으로 다른 레시피를 또한 추천받을 수 있습니다.<br>
- 사이트 링크: [http://cookalone.site](http://cookalone.site)
(현재 비용상의 문제로 서버를 내린 상태입니다)

## 1. 제작 기간 & 참여 인원
- 2022.06.02 ~ 2022.06.13
- 팀 프로젝트(4명)

## 2. 사용 기술
<div style="display:flex">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
      <img src="https://img.shields.io/badge/MySQL-4169E1?style=for-the-badge&logo=MySQL&logoColor=white">
</div>

## 3. 아키텍쳐 및 ERD 설계
- EC2를 사용해 프론트, 백 한번에 배포
<img src="https://velog.velcdn.com/images/tasha_han_1234/post/1cd07421-bafb-4b63-9a39-7926e41e7405/image.png">

## 4. 핵심 기능
<details close>
  <summary><b>📌 레시피 조회</b></summary>
- 사용자는 작성된 레시피의 목록을 조회하고, 목록 중 원하는 레시피 카드를 클릭하여 레시피의 상세 내용을 볼 수 있습니다.<br>
- 사용자는 조회한 레시피의 재료 및 조리시간, 난이도, 조리순서 등을 확인할 수 있습니다.<br>
- 사용자는 검색, 정렬, 필터 기능을 사용하여 원하는 레시피를 찾아서 확인할 수 있습니다.<br>
- 2000여개에 달하는 레시피를 서버 부하를 줄이며 보여주기 위해 장고 페이지네이션 기능을 사용했습니다.<br>
</details>
<details close>
  <summary><b>📌 레시피 추천</b></summary>
   Mecab 토크나이저를 사용해 레시피를 키워드로 나누고 이를 벡터모델을 사용해 유사한 다른 레시피를 추천했습니다. 결과적으로 96%이상에 육박하는 높은 정확도를 보였습니다.
</details>
<details close>
  <summary><b>📌 마이페이지</b></summary>
  -내가 작성한 글, 댓글, 북마크한 요리를 모아볼 수 있습니다<br>
  -랜덤한 요리 레시피 이미지가 뜨는 기능을 구현했습니다.  
</details>
<details close>
  <summary><b>📌 레시피 작성</summary>
- 로그인 한 사용자는 이미지를 포함한 레시피를 작성할 수 있습니다
- 로그인 한 사용자는 다른이용자가 작성한 게시물에 댓글을 작성 할 수 있으며, 좋아요도 달 수 있습니다
</details>
<details close>
  <summary><b>📌 회원가입, 로그인 및 기타 CRUD</b></summary>
- 사용자는 사이트 자체에서 회원가입과 로그인을 사용하여 웹에 접근할 수 있습니다.
- 회원가입은 아이디, 비밀번호, 닉네임을 기입하여 회원가입 버튼을 클릭해서 회원 데이터를 저장합니다. 
</details>


## 5. 핵심 트러블 슈팅

#### 콘텐츠 기반 추천기능 vscode적용시 환경 문제

추천 기능을 colab에서 구현한 뒤 이를 작업하던 vscode환경으로 불러오는 과정에서 난항을 겪었습니다.<br> 핵심적인 패키지가 버전이 맞지 않고 인스톨되지 않아 생긴 오류였습니다.<br> 고심끝에 추천이 된 레시피 1만개를 csv 데이터로 만든 뒤 가져와서 db에 저장하는 방식으로 해결할 수 있었습니다.<br> 돌아가는 방식이지만 창의적인 아이디어로 해결할 수 있었다고 생각합니다. <br>


#### [페이지네이션과 필터링 기능 중첩으로 생긴 버그](https://velog.io/@tasha_han_1234/%EC%8A%A4%ED%8C%8C%EB%A5%B4%ED%83%80-%EB%82%B4%EC%9D%BC%EB%B0%B0%EC%9B%80%EC%BA%A0%ED%94%84-612-%EC%9D%BC%EC%9A%94%EC%9D%BC)
    
기존에는 필터링이 여러개의 views.py함수에 분산되어 있었고, 페이지네이션이 필터링 코드보다 상단에 있었기 때문에 일어난 일이었습니다<br> 
한참을 고민한 끝에 만들어둔 필터링을 전면 수정해서 코드 상단에 필터링을 만들어 두었고, 아래에 페이지네이션 기능이 올 수 있도록 했습니다<br> 
서치를 했을 때,필터 기능을 사용했을 때,그냥 들어왔을 때 3가지 경우의 수를 나누고 각각의 결과에 따른 레시피 리스트 혹은 쿼리셋을 받아 페이지네이션을 통과하게 했습니다.<br> 
지금 봤을땐 쿼리파라미터를 사용하지 않아 불필요하게 긴 코드지만, 로직을 생각하는 방법을 배울 수 있었다는 점에서 의미 있었다고 생각합니다.


## 6. 기타 트러블 슈팅
<details close>
    <summary><b>📌 발표시 긴장하는 문제</b></summary>
  발표를 담당하게 되었는데 평소 발표할때 긴장하는 경우가 많아서 부담이 많이 되었습니다.
  대본 없이 자연스럽게 말할 수 있을것 같지 않아 대본을 2시간동안 입으로 소리내서 발표 연습을 했습니다. 
  발표를 무리 없이 끝낼 수 있었을 뿐만 아니라 주위 사람들에게 발표를 잘 한다는 평을 들을 수 있었습니다. 
</details>
<details close>
    <summary><b>📌 배포</b></summary>
  마지막 날에 배포를 하는데 아직 익숙하지 않아서 최대한 빠른 속도로 AWS강의를 듣고 
  사실 기본적인 [리눅스 명령어](https://velog.io/@tasha_han_1234/%EC%8A%A4%ED%8C%8C%EB%A5%B4%ED%83%80-%EB%82%B4%EC%9D%BC%EB%B0%B0%EC%9B%80%EC%BA%A0%ED%94%84-614-%EC%9E%A5%EA%B3%A0-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%B0%9C%ED%91%9C%EC%A0%84%EB%82%A0)도 익숙하지 않았는데 이날 많이 배울 수 있었다.
</details>
<details close>
    <summary><b>📌이미지 업로드</b>(https://www.youtube.com/watch?v=YBdpKxFi4pM)</summary>
  당시 아직 imagefield, filefield를 사용해보지 못해 이미지 업로드 하는 전체 과정이 난이도 있게 다가왔다.
  처음으로 영어 유튜브 튜토리얼을 보고 따라해본 뒤 다른 팀원들에게 이미지 업로드에 대해 알려주는 시간을 가졌습니다
</details>


## 7. 성장 & 회고
그 동안 해보고 싶었던 다양한 기능들을 시도해 볼 수 있었고,<br> 구글링을 통해 바닥부터 시작해서 하나씩 구현해 나가는 재미를 느낄 수 있었습니다. <br>
그 외에도 팀원들 디버깅을 도와주는 경험을 통해 문제 해결 능력을 키울 수 있었습니다.<br>
스스로 독립적으로 해나갈 수 있는 범위가 커지면서 코딩에 대한 자신감도 커졌다는 점이 가장 가치있었습니다.<br> 


