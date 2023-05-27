# 1. [Every-Mp3](<https://docs.e-mp3.kro.kr/main>)

<!DOCTYPE html>
<html lang="ko">
    <body>
        <div align="center">
            <a href="https://discord.com/developers/docs/intro">
                <img id="im" src="https://img.shields.io/badge/Discord-5865F2?style=flat-square&logo=Discord&logoColor=white" style="border-radius: 5%; object-fit: cover;"/>
            </a>
            <a href="http://python.org">
                <img id="im" src="https://img.shields.io/badge/Python 3.11-3776AB?style=flat-square&logo=Python&logoColor=white" style="border-radius: 5%; object-fit: cover;"/>
            </a>
            <br></br>
            <img id="Profile" src="DB/image/e-mp3-bot-full-profile.png" style="border-radius: 25%; object-fit: cover; width: 80%; height: 80%; aspect-ratio: 1; box-shadow: 0px 0px 15px #a8a39c;">
            <br></br>
            <br></br>
        </div>
    </body>
</html>

## 1.1. 소개

EP3봇은 단순이 음악을 즐기는 것 뿐만 아니라,  여러분에게 새롭고 멋진 경험을 드리기 위해 제작되었어요!🎵💝

- 📅  매달 새로운 플리의 업데이트

    매달 새로운 추천되는플레이리스트로 여러분의 감성을 채워볼까요?

- 💝 공유의 즐거움

    홀로 음악을 즐기기에도 좋지만 누군가와 함께 나누는 것은 특별한 경험을 남겨주어요.😊
    여러분만의 음악 감성을 담은 플레이리스트를 다른 이들과 함께 공유하여, 새로운 곡을
    찾는 특별한경험을 하게 될지도 몰라요. 이를 통해 공유의 즐거움을 더욱 느끼실 수 있을 거예요! 😀

- 😎 멋진 앨범 커버

    이 기능은 이 봇을 개발하게 된 계기와도 마찬가지인 기능 이에요.
    투박하고 딱딱한 디스코드 임베드(Discord Embed) 대신
    여러분의 플레이리스트를 빛나게  해줄, 딱 알맞는 멋진 앨범 커버 이미지를 자동으로 생성해 주어, 세련된 경험을 느껴 보실 수 있어요! ✨

    또한, 이렇게 생성된 앨범 커버 이미지는 CC BY-NC(저작자표시 및 비영리) 형태의
    저작권을 가지게 되어, 비영리 목적이라면 어디든 사용해도 좋아요🐬

- 🔥개성 있는 인기 플리

    평소 들어보지 못했던 곡이나, 최신 음악 트렌드 곡들을 듣기에 알맞는 기능이에요.
    여러분의 멋진 플레이리스트도 인기 상승 리스트에 올라가게 되길 바라요! 🥳
    ​

- ☁️ 마무리

    언제나 여러분의 경험을 중요시하며, 더 나은서비스를 제공하기 위해 최선을 다하고 있습니다.
    여러분의 소중한 의견은 언제나 환영하며, 더욱 더 나은 봇으로 발전할 수 있도록 노력하겠습니다.
    감사합니다! 🙏🎵

🚠[튜토리얼](<https://docs.e-mp3.kro.kr/main>) 시작하기!  

📸profile image by [Midjourney](<https://midjourney.com/>)  
ⓒ 2023. ManGGo.ß STUDIO All rights reserved.  

- [1. Every-Mp3](#1-every-mp3)
  - [1.1. 소개](#11-소개)
  - [1.2. TODO](#12-todo)
  - [1.3. DEV ROADMAP](#13-dev-roadmap)
  - [1.4. config 설정](#14-config-설정)
  - [1.5. 용어](#15-용어)
  - [1.6. 플리](#16-플리)
    - [1.6.1. 플리 타입](#161-플리-타입)
    - [1.6.2. 플리 관련 클래스](#162-플리-관련-클래스)
    - [1.6.2.1. PlaylistManager](#1621-playlistmanager)
    - [1.6.3. 조작](#163-조작)
    - [1.6.3.1 플리 생성](#1631-플리-생성)
  - [1.7. 명령어 목록](#17-명령어-목록)
  - [1.8. UI](#18-ui)
    - [1.8.1. 재생중](#181-재생중)
  - [1.9. 데이터 저장 (DBMS)](#19-데이터-저장-dbms)
    - [1.9.1. DBMS](#191-dbms)
      - [1.9.1.1 용어](#1911-용어)
      - [1.9.1.2. Instruction](#1912-instruction)
      - [1.9.1.3. 전체 과정](#1913-전체-과정)
    - [1.9.2. 플리 집계 및 저장](#192-플리-집계-및-저장)
    - [1.9.3. 플리의 저장 및 백업](#193-플리의-저장-및-백업)
    - [1.9.4. 플리의 비공개 \<-\> 공개](#194-플리의-비공개---공개)
    - [1.9.5. Json 형식](#195-json-형식)
    - [1.9.6. 기타 데이터 형식](#196-기타-데이터-형식)
  - [1.10. 지금까지 발견된 에러](#110-지금까지-발견된-에러)
  - [1.11. 추후 업데이트로 할만한 아이디어.zip ..?](#111-추후-업데이트로-할만한-아이디어zip-)
    - [1.11.1. 플리 라이브](#1111-플리-라이브)
    - [1.11.2. 새로운 인기도 시스템](#1112-새로운-인기도-시스템)
    - [1.11.3. 유저 맞춤 플리 추천](#1113-유저-맞춤-플리-추천)

## 1.2. TODO

- [x] : 집계 view listen 일일, 월간, 주간 방식 고민하기
- [x] : 하트를 유튜브 좋아요 처럼(일일/주간/월간 인기 방식 고안) 1번만 or 12시간에 한번 투표 같은 형식(어뷰징 가능성⇑..) or 기타 방법 고안해보기.. -> 차라리 그냥 플리를 장르별로 검색/추천, 시청횟수랑 추천알고리즘 기반으로? / ->집계공식도 수정필요<-
    -> 하트는 1번만 가능함
    -> 일일/주간/월간의 주목적은 기일내 인기가 상승중인 플리를 표시하기 위함
    -> 집계 공식은 X
- [x] : json 데이터 형식 지정
- [x] : 플리가 공개 <-> 비공개인 경우 어떻게 할까..? -> 공개 -> 비공개인 경우 금일에는 집계하고, 다음날 부턴 집계 하지 않음, 비공개 -> 공개인 경우에는 똑같이 집계함

## 1.3. DEV ROADMAP

.**위 부터 순서대로 구현**

- 클래스 & 라이브러리
    - [x] : logger.py
    - [x] : FileIO.py
    - [ ] : Instruction.py
        - [ ] playlist 관련 함수
        - [ ] user 관련 함수
        - [ ] 요청 생성 함수
    - [x] : DBMS.py
        - [x] : link FileIO.py  
        - [x] : link Instruction.py  
        - [x] : using multiprocessing to make auto data updating  
    - [ ] : Playlist.py (class)
        - [x] : 이미지 생성 (앞 장)
        - [ ] : 이미지 생성 (뒷 장)
        - [ ] : 기능 구현
    - [x] : Task.py

1. 약관 동의/철회 (lib.terms.py)
    - [ ] : 약관 검사 모듈 구현
    - [ ] : 약관 동의 기능 구현
    - [ ] : 역관 철회 기능 구현

2. 플리 기본 기능 (플리 클래스)
    - [ ] : 플리 생성 기능 구현
    - [ ] : 변경사항 저장/삭제 기능 구현
    - [ ] : 플리 삭제 기능 구현
    - [ ] : 곡 검색 기능 구현
    - [ ] : 플리 곡 추가와 곡 검색 기능 연동
    - [ ] : 플리 곡 위치 변경 구현
    - [ ] : 플리 곡 삭제 기능 구현
    - [ ] : 플리 커버 이미지 설정 기능 구현

3. 플리 관리 UI
    - [ ] : 내 플리 다음/이전 기능 구현
    - [ ] : 플리 선택 기능과 다음/이전 기능 연동

4. 플리 집계
    - [ ] : X

5. `/플리`
    - [ ] : `/플리 [추천/일일/주간/월간]` 기능 구현
    - [ ] : `/플리 [추천/일일/주간/월간]`와 `/플리` 자세히보기 (셀렉트) 연동
    - [ ] : 플리 자세히 보기 구현
    - [ ] : `/플리` 플리 다음/이전 기능 구현
    - [ ] : `/플리` 플리 선택 기능 구현
    - [ ] : 외부 플리 표시 모듈 구현
    - [ ] : 플리 하트 기능 구현

6. 이미지 생성
    - [x] : 플리 정보 IMAGE 생성 (첫페이지)
    - [ ] : 플리 정보 IMAGE 생성 (모든 뒷페이지)
    - [ ] : 내 플리 IMAGE 생성 모듈 구현
    - [ ] : 인기 플리 IMAGE 생성 모듈 구현
    - [ ] : 음악재생 화면 생성 모듈 구현

7. 플리 및 음악 재생
    - [ ] : 재생 UI 구현
    - [ ] : 큐
    - [ ] : 이전 기능 구현
    - [ ] : 중지 기능 구현
    - [ ] : 다음 기능 구현
    - [ ] : 시간조정(seek) 기능 구현
    - [ ] : 점프 기능 구현
    - [ ] : 하트 시스템 연동

8. (last) 도움말 명령어 및 페이지
    - [ ] : `/도움말` 구현
    - [ ] : `/도움말 [검색어]` 구현
    - [ ] : 도움말 페이지 제작

9. 유저 기본 기능 (유저 클래스)
    - [ ] : X

## 1.4. config 설정

- `start_total` : `True/False` : 봇의 시작시 집계 여부
- `end_total` : `True/False` : 봇의 종료시 집계 여부

## 1.5. 용어

일일 PICK 플리 -> 작일 인기 플리
주간 PICK 플리 -> 최근 1주 동안 인기 플리  
월간 PICK 플리 -> 최근 1달(30일) 동안 인기 플리  
이번달의 추천 플리 -> 매달 만들어 지는 추천 플레이리스트 (내가 직접 추가 해야됨)  
명령어내 -> `/명령어이름 [a/b] <1/2>` 형태
명령어내 **대괄호**( **[ ]** ) -> 선택적 옵션  
명령어내 **꺾쇠괄호** ( **<>** ) -> 필수 옵션  
명령어내 **슬래시** ( **/** ) -> 옵션 구분
하트 -> 즐겨찾기와 비슷한 기능, 및 최근에 좋아요를 많이 받을 수록 인기 상승 목록에 게재됨

## 1.6. 플리

### 1.6.1. 플리 타입

- 비공개형 -> 집계 시스템에 포함되지 않는 플리(단 공개형->비공개형 전환시 그 다음 날에는 집계함)
- 공개형 -> 집계 시스템에 포함되어 하트 집계가 이루어 지는 플리
- 저장형 -> 플리의 제목, 커버, 곡 추가등 기본 기능은 가능하지만, 비공개형 <-> 공개형 전환은 불가능하며 비공개형으로 항상 유지

### 1.6.2. 플리 관련 클래스

### 1.6.2.1. PlaylistManager

플리 관리 및 기능 함수 모음

### 1.6.3. 조작

플레이리스트의 생성 / 삭제 등의 모든 과정

### 1.6.3.1 플리 생성

1. (유저) 유저가 생성 버튼/명령어를 입력
2. (유저) 플리의 타이틀 작성
3. (유저) 플리의 설명 작성
4. (유저) 플리의 공개여부 설정
5. (유저) 음악 추가 . 검색 -> 선택 -> 곡 타이틀 확인 -> 곡 저자 확인 -> 추가 (반복)
6. (유저) 플리의 커버 이미지 선택 -> 여러 곡들중 썸네일 또는 기본 커버 이미지  
~~7. (유저) 플리의 배경 타입 설정~~
7. (시스템) 플리 UUID 생성
8. (시스템) 생성시간 기록
9. (시스템) 생성 시간 기록
10. (시스템) 곡 개수 카운트
11. (시스템) 곡 총 시간 합
12. (시스템) JSON 저장 요청 -> DataManager
13. (시스템) Playlist.User 클래스 생성
14. (시스템) Playlist.User.Image.create_image()
15. (시스템) Playlist.User.Image.write_image()
16. (시스템) 결과 표시

## 1.7. 명령어 목록

모든 명령어는 유저가 개인정보 처리방침 및 이용약관을 동의했을때만 사용이 가능하며  
그 외의 경우에는 `/약관동의` 라는 명령어와 같은 페이지를 띄운다.  

- `/도움말` -> 도움말
- `/가입` -> 개인정보 처리방침 및 이용약관 동의 및 유저 데이터 생성
- `/탈퇴` -> 약관 철회 및 유저 데이터 (discord_id, 시청시간, 생성 플리, 청취 플리, 청취 음악, 청취 지속시간, 플리 하트, 및 기타 자동으로 생성된 맞춤 데이터), 유저 데이터는 삭제 요청 시일로부터 최대 7일간 유지되며 7일이내 `/약관동의` 명령어를 재사용시 복구가 가능함.

1. `/플리 pick:[기본/일일 PICK/주간 PICK/월간 PICK/전체 PICK]` -> 추천 & 일일 인기 플리 & 이번달의 추천 플리 1개 표시 또는 옵션에 따라 표시, 아래 버튼 (버튼 `🔍 자세히 보기`, `내플리`, `플리 재생`)  
2. `/플리 검색` -> 플리 검색(장르/검색어 기반)
3. `/플리 추천` -> 이번달의 추천 플리 표시, (버튼 `🔍 자세히 보기`, `🎶 재생하기`, `📜 저장하기`)  
4. `/플리 관리` -> 최상단 하트 플리( 2 x 2 크기, 없을경우 두칸의 빈 공간 표시) 하단 또는 뒷페이지 일반플리들(순서는 이름순) , (버튼 `플리 만들기`, `플리 삭제하기`, `<--`, `-->`), (셀렉트 -> 플리(해당페이지))
5. `/플리 하트` -> 하트 누른 플리 표시 (셀렉트 '관리할 플리 선택' `하트 누른 플리 표시`) -> (버튼 `🔍 자세히 보기`, `🎶 재생하기`, `💔 취소하기`, `📜 저장하기`))  

## 1.8. UI

자세한 내용은 **e-mp3(bot)_ProgrameUIDesign.clip** 참고하기  
![ProgrameUIDesign]( e-mp3(bot)_ProgrameUIDesign.png "e-mp3(bot)_ProgrameUIDesign.png")

### 1.8.1. 재생중

플리 재생중에는 아래에 `중단`, `건너뛰기`, `점프`, `하트`, `저장하기`, `종료` 와 같은 버튼 표시  

## 1.9. 데이터 저장 (DBMS)

플리 데이터와 유저 데이터를 구분하여 저장하고,  
플리에는 각각의 고유 번호를 부여하여  
해당 플리를 가지고 있는 유저에겐 플리 ID를, 플리에는 유저 ID를 저장,  

- 날자 및 시간의 표기는 `년.월.일.시간.분.초` 또는 `년.월.일` 로 저장함

### 1.9.1. DBMS

#### 1.9.1.1 용어

- 작업 큐(Task.QueueManager): 각 스레드에 균등하게 작업을 분배 시키기 위해, 요청이 들어오면 작업이 가장 적은 큐를 선택하여, 작업 요청을 추가 하는 형태로 작동하는 Class  

- 작업 객체 상태(Task.StatusManager): 업을 추적하기 위해, 작업 객체는 작업에 대한 정보와 상태를 포함하고, 작업이 완료되면 해당 객체의 상태를 업데이트. 작업 객체에 '대기 중(waiting)', '진행 중(in progress)', '완료(done)', '실패(failure)'와 같은 상태를 부여하여 작업 상태를 확인 가능

#### 1.9.1.2. Instruction

- user
    생성: create, 삭제: delete, 수정: alter
    1. create_account : 유저 가입
    2. delete_account : 유저 탈퇴
    3. alter_nickname : 닉네임 변경
    4. add_kdbl_point : 한디리 하트 포인트 추가
    5. alter_terms_pp : 개인정보 처리방침 동의 여부 수정
    6. alter_terms_tos : 이용약관 동의 여부 수정
    7. alter_trems_mc : 광고성 정보 수신 동의 여부 수정
    8. add_playlist : 플리 추가
    9. delete_playlist : 플리 삭제
    10. add_bookmark : 북마크 추가
    11. delete_bookmark : 북마크 삭제

- playlist  
    생성: create, 삭제: remove, 수정: alter
    1. create_playlist : 플리 생성
    2. remove_playlist : 플리 삭제
    3. alter_name : 이름 수정
    4. alter_description : 설명 수정
    5. alter_using_custom_cover_img : 커스텀 이미지 사용여부 수정
    6. alter_cover_img : 커버 이미지 수정
    7. alter_visibility : 공개여부 수정
    8. add_music : 음악 추가
    9. remove_music : 음악 삭제
    10. add_heart : 하트 추가
    11. alter_dominant_color : 대표색 수정
    12. alter_background_type : 배경 타입 변경

#### 1.9.1.3. 전체 과정

- 준비

1. Instruction.CreateInstruction.~ 으로 요청데이터(명령어 종류, 사용자 정보, 작업에 필요한 데이터를 포함)를 생성

- 요청

1. 생성된 요청 데이터를 DBMS에 PUT
2. 작업 큐(Task.QueueMananger.put_task)에 작업 요청 추가
3. 작업 요청의 상태 추가 (Task.StatusManager.add_task)

- 실행

1. 작업 요청 상태 - 실행 중 변경
2. 분배된 작업요청을 멀티프로세싱(multiprocessing) 으로 실행

- 완료

1. 작업 요청 상태 - 완료/실패/comment 변경 (해당 함수에서 추가 / Instruction.Instruction)

### 1.9.2. 플리 집계 및 저장

1. 집계의 기준
    - 플리는 매일 자정(00:00 ~ 00:10±a)에 집계함  
    - 집계는 봇 시스템 내부에 비동기 클래스로 봇이 시작될 때 self.bot 변수에 포함함. (시작시 시간을 확인하고 자정까지 시간(-1분)을 계산해 wait, 1분 전부터는 초단위로 wait함)
    - `/도움말` 명령어를 제외한 **모든 명령어는 사용이 불가**
    - visibility_playlist.json 에 public 인 데이터만 집계

2. 플리의 집계
    - 하트는 today(Integer) 와 last(Obj) 그리고 all(Integer)의 세 변수로 플리 데이터 내부에 저장함
    1. last.update({"년.월.일" : today})
    2. all += today
    3. today = 0
    4. week = last[:7] (최근 7일) (단 1번 작업이 된 last 기준.)
    5. month = last[:30] (최근 30일) (단 1번 작업이 된 last 기준.)
    6. all 집계

3. 비공개/공개 여부가 바뀐 플리의 집계
    - 공개 -> 비공개 플리
        (visibility_playlist.json[public_to_private] 에 있는 플리들)  
       -> 집계후 public_to_private 에서 삭제

    - 비공개 -> 공개 플리
        X 그냥 일반대로 집계

4. 랭킹 집계
    1. 모든 플리의 day, week, month, all 집계하여 순서를 매김 (total_(day/week/month/all).json)
    2. 일일 PICK 초기화 후 집계(전날기준)

5. 삭제 예정인 플리
   1. BeDeleted.json 에서 BeDeleted 값을 모두 확인하며 date 가 오늘 날짜 (date-type2) 와 같으면 삭제
   2. 그후 playlist에도 uuid 제거

### 1.9.3. 플리의 저장 및 백업

1. 플리의 저장  
    - 플리는 저장시 json(<-> dict) 형식으로 저장함  
    - 플리에 저장하는 항목은 아래 플리 데이터 참고
    - 공개여부(Visibility) 는 0 -> 비공개, 1 -> 공개 처리함  
    - 플리에 음악 저장시 `제목`, `영상 url`, `시간`, `제작자`, `제작자 채널 url`, `미리보기 이미지 url` 등을 저장함  

2. 플리의 백업  
    - 플리는 매일 집계시간마다 백업되며 최대 1주일 까지 백업됨  
    - 유저가 플리 삭제 요청시 최대 1주일 까지 백업

### 1.9.4. 플리의 비공개 <-> 공개

1. 플리가 비공개 -> 공개인 경우
    visibility_playlist.json[private_to_public] 에 추가함

2. 플리가 공개 -> 비공개인 경우
    visibility_playlist.json[public_to_private] 에 추가함

### 1.9.5. Json 형식

플리 데이터와 유저 데이터 및 집계 데이터는 각각 다음과 같은 방식으로 저장함.  

1. 플리 데이터 (heart/noheart.playlist_uuid.json)

    ```json
    {
        "InstructName" : "사용된 명령어 이름(DBMS에서 자동으로 생성되는 항목)",
        "Identifier" : "식별자(DBMS에서 자동으로 생성되는 항목)",
        "name" : "<플리 이름>",
        "description" : "<플리 설명>",
        "using_custom_cover_img" : "<커스텀 커버 이미지 사용여부(True/False)>",
        "cover_img" : "<플리 커버 이미지 파일명(userID_playlist_uuid)> 또는 기본 커버 이름(default_<number>)>", 
        "cover_img_dominant_color" : "<커버 이미지의 대표색>",
        "alter_background_type" : 1,
        "playlist_uuid" : "<플리 고유 ID>",
        "owner_id" : "<소유자(유저) 디스코드 고유 ID>",
        "visibility" : "<공개여부|False:비공개/True:공개)",
        "first_date" : "<플리 최초 작성 날짜 및 시간 date-type4>",
        "last_date" : "<플리 최종 수정 날짜 및 시간 date-type4>",
        "official" : "<공식플리 여부|False/True>",
        "music" : [
            {
                "title" : "<영상의 제목>",
                "link" : "<영상의 url>",
                "time" : "<영상의 총 길이>",
                "author" : "<영상 업로더>",
                "author_link" : "<업로더 채널 url>",
                "thumbnail" : "<미리보기 이미지 url>",
                "c_name" : "<곡명> (유저지정/이미지 생성에 사용)",
                "c_singer" : "<가수명> (유저지정/이미지 생성에 사용)"
            }
        ],
        "heart" : {
            "today" : ["user_id"],  // 당일 받은 하트 수는 유저 ID 가지고 카운트
            "last" : [
                {"date-type2" : 0} // `년/월/일`(date-type2) 에 받은 하트 수
            ],
            // 아래 두 항목은 집계시 초기화 후 last 를 이용해 계산
            "week" : 0, // 주간 인기 (7일 기준)
            "month" : 0, // 월간 인기 (31일 기준)
            "all" : 0, // 종합
        }
    }
    ```

2. 유저 데이터 (user_id.json)

    ```json
    {
        "InstructName" : "사용된 명령어 이름(DBMS에서 자동으로 생성되는 항목)",
        "Identifier" : "식별자(DBMS에서 자동으로 생성되는 항목)",
        "user_id" : "<소유자(유저) 디스코드 고유 ID>",
        "nickname" : "플리 공유상의 닉네임",
        "kdbl_point": 0, // 한디리(Korean discrod bot list) 하트 포인트
        "terms" : {
            "policy_privacy" : false, // 개인정보 처리방침 동의 여부
            "terms_of_service" : false, // 이용약관(tos) 동의 여부
            "marketing_consent" : false, // 광고성 정보 수신 동의 여부
        },
        "playlist" : [
            "uuid", // playlist uuid
            "uuid",
        ]
    }
    ```

3. 집계 데이터 (total_(day/week/month/all).json)

    각 total_day.json / total_week.json / total_month.json / total_all.json 으로 존재함.  
    처음에는 is_sort 상태가 아닌 상태로 저장하고(또는 메모리상으로 바로) 각각 4개를 쓰레드로 순위를 매겨 저장

    ```json
    {
        "is_sort" : false, // 플리의 순위가 매겨졌는지 여부
        "rank" : {
            // "순위": {"uuid" : "score"}
        }
    }
    ```

4. 플리의 공개/비공개 데이터 (visibility_playlist.json)

    ```json
    {
        "public" : ["uuid" ... "uuid"],
        "public_to_private" : ["uuid" ... "uuid"],
        // "private_to_public" : ["uuid" ... "uuid"] 은 없고 바뀌면 바로 public 에 추가됨
    }
    ```

5. 삭제 예정 플리 데이터 (BeDeleted.json)

    ```json
    {
        "BeDeleted" : {
            "user_id(int)" : { 
                "date" : "요청일 기준 + 7일(date-type2)",
                "playlist" : "uuid"
            }
        },
        "playlist" : ["uuid", ...] // 삭제 예정인 플리
    }
    ```

<!-- 
1. 일반 데이터 (data.json)

플리의 비공개/공개가 바뀌었거나 기타 등등 해당 집계시간에 한번 실행해야 하는 것들

    ```json
    {
        "playlist" : {
            "visibility_will_true" : ["uuid"],
            "visibility_will_false"s : ["uuid"]
        }
    }
    ``` -->

### 1.9.6. 기타 데이터 형식

1. 시간 타입 (date type)
    1. type1 : 유닉스 타임스탬프
    2. type2 : 년/월/일
    3. type3 : 시.분.초
    4. type4 : 년/월/일-시.분.초

## 1.10. 지금까지 발견된 에러

- [x] : 23/2/17-21:32 -> 23/2/19-01:30 stage 채널 접속시 자동으로 연설자로 되지 않는 현상
- [x] : 23/2/18-22:56 -> 23/2/19-01:30 stage 가 종료됐을때, DefaultPlayer가 파괴되지 않고, 다른 채널에서 `/연결` 명령어를 사용할 시 이어서 노래가 재생되는 현상
- [x] : 23/2/19-14:9 -> stage 채널에서 `/연결` 명령어 사용시 이미 연결이 되어 있더라도 연결되었다고 출력되는 현상
- [ ] : ?

## 1.11. 추후 업데이트로 할만한 아이디어.zip ..?

### 1.11.1. 플리 라이브

- `/플리 라이브` -> 라이브로 재생되는 플리 (like Radio)

### 1.11.2. 새로운 인기도 시스템

    이런 형식으로 view 와 listen 의 횟수를 기록하여 합산하는 방식..

```json
    "view" : {
        "today" : 0, // 당일 본 조회수 / 1시간 기준으로 +1
        "view_one_hour_user" : [
            // user_id : time.time()
        ], // 최근 본 유저를 1시간 동안 저장, 만약 그 유저가 1시간이 지난후에 다시 보면 그 시간으로 변경, time.time() 시간 기준, 
        "last" : [
            {"2023.1.1" : 0} // `년.월.일` 에 받은 하트 수
        ],
        // 아래 두 항목은 집계시 초기화 후 last 를 이용해 계산
        "week" : 0, // 주간 조회수 (7일 기준)
        "month" : 0, // 월간 조회수 (31일 기준)
    },
    "listen" : {
        "today" : 0, // 청취 횟수 (1곡의 1/2 이상 청취시 카운트 +1) / 당일에는 최대 6회까지만
        "listen_today_user" : [
            // user_id : count
        ],
        // 아래 두 항목은 집계시 초기화 후 last 를 이용해 계산
        "week" : 0, // 주간 청자 (7일 기준)
        "month" : 0, // 월간 청자 (31일 기준)
    }
```

를 기반으로 이런 형식의 집계 시스템 구성

- SCORE : 종합적인 점수값
- V : view
- L : listen
- P : view-listen-per (listen / view)
- H : heart
$${Score} = (0.8{V}+L)\frac{L}{V} + 0.75{H} $$

### 1.11.3. 유저 맞춤 플리 추천

- `/플리` 명령에 유저 맞춤 플리 추천
