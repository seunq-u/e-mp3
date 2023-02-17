# Every-Mp3

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

## 간단한 설명

🗓️ 매달 업데이트 되는 플리와 여러분만의 소중한 💝 플리를  
공유하거나 재생 할 수 있는 봇 이에요! 🎵  
🚠[튜토리얼](<https://docs.e-mp3.kro.kr/>) 시작하기!  

📸profile image by [Midjourney](<https://midjourney.com/>)  
ⓒ 2023. MaenGGo.ß STUDIO All rights reserved.  

- [Every-Mp3](#every-mp3)
  - [간단한 설명](#간단한-설명)
  - [TODO](#todo)
  - [DEV ROADMAP](#dev-roadmap)
  - [config 설정](#config-설정)
  - [용어](#용어)
  - [플리 타입](#플리-타입)
  - [명령어 목록](#명령어-목록)
  - [UI](#ui)
    - [재생중](#재생중)
  - [데이터 저장 (DataManager)](#데이터-저장-datamanager)
    - [DataManager](#datamanager)
      - [Instruction](#instruction)
    - [플리 집계 및 저장](#플리-집계-및-저장)
    - [플리의 저장 및 백업](#플리의-저장-및-백업)
    - [플리의 비공개 \<-\> 공개](#플리의-비공개---공개)
    - [Json 형식](#json-형식)
    - [기타 데이터 형식](#기타-데이터-형식)
  - [추후 업데이트로 할만한 아이디어.zip ..?](#추후-업데이트로-할만한-아이디어zip-)
    - [플리 라이브](#플리-라이브)
    - [새로운 인기도 시스템](#새로운-인기도-시스템)
    - [유저 맞춤 플리 추천](#유저-맞춤-플리-추천)

## TODO

- [x] : 집계 view listen 일일, 월간, 주간 방식 고민하기
- [x] : 하트를 유튜브 좋아요 처럼(일일/주간/월간 인기 방식 고안) 1번만 or 12시간에 한번 투표 같은 형식(어뷰징 가능성⇑..) or 기타 방법 고안해보기.. -> 차라리 그냥 플리를 장르별로 검색/추천, 시청횟수랑 추천알고리즘 기반으로? / ->집계공식도 수정필요<-
    -> 하트는 1번만 가능함
    -> 일일/주간/월간의 주목적은 기일내 인기가 상승중인 플리를 표시하기 위함
    -> 집계 공식은 X
- [ ] : json 데이터 형식 지정
- [x] : 플리가 공개 <-> 비공개인 경우 어떻게 할까..? -> 공개 -> 비공개인 경우 금일에는 집계하고, 다음날 부턴 집계 하지 않음, 비공개 -> 공개인 경우에는 똑같이 집계함

## DEV ROADMAP

.**위 부터 순서대로 구현**

- 클래스 & 라이브러리
    - [x] : logger.py
    - [ ] : FileIO.py
    - [ ] : Instruction.py
    - [ ] : DataManager.py
        1. link FileIO.py
        2. link Instruction.py
        3. using multiprocessing to make auto data updating
        4. From json file get data
    - [ ] : Playlist.py (class)

1. 약관 동의/철회 (lib.terms.py)
    - [ ] : 약관 검사 모듈 구현
    - [ ] : 약관 동의 기능 구현
    - [ ] : 역관 철회 기능 구현

2. 플리 관리 기능
    - [ ] : 플리 생성 기능 구현
    - [ ] : 변경사항 저장/삭제 기능 구현
    - [ ] : 플리 삭제 기능 구현
    - [ ] : 곡 검색 기능 구현
    - [ ] : 플리 곡 추가와 곡 검색 기능 연동
    - [ ] : 플리 곡 위치 변경 구현
    - [ ] : 플리 곡 삭제 기능 구현
    - [ ] : 플리 커버 이미지 설정 기능 구현
    - [ ] : 플리 즐겨찾기 구현

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

## config 설정

- `start_total` : `True/False` : 봇의 시작시 집계 여부
- `end_total` : `True/False` : 봇의 종료시 집계 여부

## 용어

일일 PICK 플리 -> 작일 인기 플리
주간 PICK 플리 -> 최근 1주 동안 인기 플리  
월간 PICK 플리 -> 최근 1달(30일) 동안 인기 플리  
이번달의 추천 플리 -> 매달 만들어 지는 추천 플레이리스트 (내가 직접 추가 해야됨)  
명령어내 -> `/명령어이름 [a/b] <1/2>` 형태
명령어내 **대괄호**( **[ ]** ) -> 선택적 옵션  
명령어내 **꺾쇠괄호** ( **<>** ) -> 필수 옵션  
명령어내 **슬래시** ( **/** ) -> 옵션 구분

## 플리 타입

- 비공개형 -> 집계 시스템에 포함되지 않는 플리(단 공개형->비공개형 전환시 그 다음 날에는 집계함)
- 공개형 -> 집계 시스템에 포함되어 하트 집계가 이루어 지는 플리
- 저장형 -> 플리의 제목, 커버, 곡 추가등 기본 기능은 가능하지만, 비공개형 <-> 공개형 전환은 불가능하며 비공개형으로 항상 유지

## 명령어 목록

모든 명령어는 유저가 개인정보 처리방침 및 이용약관을 동의했을때만 사용이 가능하며  
그 외의 경우에는 `/약관동의` 라는 명령어와 같은 페이지를 띄운다.  

- `/도움말` -> 도움말
- `/가입` -> 개인정보 처리방침 및 이용약관 동의 및 유저 데이터 생성
- `/탈퇴` -> 약관 철회 및 유저 데이터 (discord_id, 시청시간, 생성 플리, 청취 플리, 청취 음악, 청취 지속시간, 플리 하트, 및 기타 자동으로 생성된 맞춤 데이터), 유저 데이터는 삭제 요청 시일로부터 최대 7일간 유지되며 7일이내 `/약관동의` 명령어를 재사용시 복구가 가능함.

1. `/플리 pick:[기본/일일 PICK/주간 PICK/월간 PICK/전체 PICK]` -> 추천 & 일일 인기 플리 & 이번달의 추천 플리 1개 표시 또는 옵션에 따라 표시, 아래 버튼 (버튼 `🔍 자세히 보기`, `내플리`, `플리 재생`)  
2. `/플리 검색` -> 플리 검색(장르/검색어 기반)
3. `/플리 추천` -> 이번달의 추천 플리 표시, (버튼 `🔍 자세히 보기`, `🎶 재생하기`, `📜 저장하기`)  
4. `/플리 관리` -> 최상단 즐겨찾기 플리( 2 x 2 크기, 없을경우 두칸의 빈 공간 표시) 하단 또는 뒷페이지 일반플리들(순서는 이름순) , (버튼 `플리 만들기`, `플리 삭제하기`, `<--`, `-->`), (셀렉트 -> 플리(해당페이지))
5. `/플리 하트` -> 하트 누른 플리 표시 (셀렉트 '관리할 플리 선택' `하트 누른 플리 표시`) -> (버튼 `🔍 자세히 보기`, `🎶 재생하기`, `💔 취소하기`, `📜 저장하기`))  

## UI

자세한 내용은 **e-mp3(bot)_ProgrameUIDesign.clip** 참고하기  
![ProgrameUIDesign]( e-mp3(bot)_ProgrameUIDesign.png "e-mp3(bot)_ProgrameUIDesign.png")

### 재생중

플리 재생중에는 아래에 `중단`, `건너뛰기`, `점프`, `하트`, `저장하기`, `종료` 와 같은 버튼 표시  

## 데이터 저장 (DataManager)

플리 데이터와 유저 데이터를 구분하여 저장하고,  
플리에는 각각의 고유 번호를 부여하여  
해당 플리를 가지고 있는 유저에겐 플리 ID를, 플리에는 유저 ID를 저장,  

- 날자 및 시간의 표기는 `년.월.일.시간.분.초` 또는 `년.월.일` 로 저장함

### DataManager

#### Instruction

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

### 플리 집계 및 저장

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

### 플리의 저장 및 백업

1. 플리의 저장  
    - 플리는 저장시 json(<-> dict) 형식으로 저장함  
    - 플리에 저장하는 항목은 아래 플리 데이터 참고
    - 공개여부(Visibility) 는 0 -> 비공개, 1 -> 공개 처리함  
    - 플리에 음악 저장시 `제목`, `영상 url`, `시간`, `제작자`, `제작자 채널 url`, `미리보기 이미지 url` 등을 저장함  

2. 플리의 백업  
    - 플리는 매일 집계시간마다 백업되며 최대 1주일 까지 백업됨  
    - 유저가 플리 삭제 요청시 최대 1주일 까지 백업

### 플리의 비공개 <-> 공개

1. 플리가 비공개 -> 공개인 경우
    visibility_playlist.json[private_to_public] 에 추가함

2. 플리가 공개 -> 비공개인 경우
    visibility_playlist.json[public_to_private] 에 추가함

### Json 형식

플리 데이터와 유저 데이터 및 집계 데이터는 각각 다음과 같은 방식으로 저장함.  

1. 플리 데이터  

    ```json (playlist_uuid.json)
    {
        "name" : "<플리 이름>",
        "description" : "<플리 성명>",
        "using_custom_cover_img" : "<커스텀 커버 이미지 사용여부(True/False)>",
        "cover_img" : "<플리 커버 이미지 파일명(userID_playlist_uuid)> 또는 기본 커버 이름(default_<number>)>", 
        "playlist_uuid" : "<플리 고유 ID>",
        "owner_id" : "<소유자(유저) 디스코드 고유 ID>",
        "visibility" : "<공개여부|False:비공개/True:공개)",
        "first_date" : "<플리 최초 작성 날짜 및 시간 date-type4>",
        "last_date" : "<플리 최종 수정 날짜 및 시간 date-type4>",
        "music" : [
            {
                "title" : "<음악의 제목>",
                "link" : "<음악의 url>",
                "time" : "<음악의 총 길이>",
                "author" : "<제작자>",
                "author_link" : "<제작자 url>",
                "thumbnail" : "<미리보기 이미지 url>",
            }
        ],
        "heart" : {
            "today" : 0,  // 당일 받은 하트 수
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
        ],
        "bookmark" : [
            "uuid" // playlist uuid
        ], // 즐겨찾기
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

### 기타 데이터 형식

1. 시간 타입 (date type)
    1. type1 : 유닉스 타임스탬프
    2. type2 : 년/월/일
    3. type3 : 시.분.초
    4. type4 : 년/월/일-시.분.초

## 추후 업데이트로 할만한 아이디어.zip ..?

### 플리 라이브

- `/플리 라이브` -> 라이브로 재생되는 플리 (like Radio)

### 새로운 인기도 시스템

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

### 유저 맞춤 플리 추천

- `/플리` 명령에 유저 맞춤 플리 추천
