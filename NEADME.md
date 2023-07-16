# - 작 업 중 -

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

EMP3봇은 단순이 음악을 즐기는 것 뿐만 아니라,  여러분에게 새롭고 멋진 경험을 드리기 위해 제작되었어요!🎵💝

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

    ***⚠️단 이렇게 생성된 앨범 커버 이미지는 생성에 사용된 원저작물(앨범아트, 곡 썸네일, 유저의 프로필 사진 등)의 저작권은 꼭 지키는 선 안에서만 이용해 주세요.⚠️***

- 🔥개성 있는 인기 플리

    평소 들어보지 못했던 곡이나, 최신 음악 트렌드 곡들을 듣기에 알맞는 기능이에요.
    여러분의 멋진 플레이리스트도 인기 상승 리스트에 올라가게 되길 바라요! 🥳

- ☁️ 마무리

    언제나 여러분의 경험을 중요시하며, 더 나은서비스를 제공하기 위해 최선을 다하고 있습니다.
    여러분의 소중한 의견은 언제나 환영하며, 더욱 더 나은 봇으로 발전할 수 있도록 노력하겠습니다.
    감사합니다! 🙏🎵

🚠[튜토리얼](<https://docs.e-mp3.kro.kr/main>) 시작하기!  

📸profile image by [Midjourney](<https://midjourney.com/>)  
ⓒ 2023. ManGGo.ß STUDIO All rights reserved.  

- [- 작 업 중 -](#--작-업-중--)
- [1. Every-Mp3](#1-every-mp3)
  - [1.1. 소개](#11-소개)
  - [1.2 용어의 정의](#12-용어의-정의)
  - [1.3 DEV ROADMAP](#13-dev-roadmap)
  - [1.4 정책](#14-정책)
    - [1.4.1 개발](#141-개발)
    - [1.4.2 운영](#142-운영)
- [2. DATA](#2-data)
  - [2.1. 개요](#21-개요)
  - [2.2. 형식](#22-형식)
    - [2.2.1. USER](#221-user)
    - [2.2.2. PLAYLIST](#222-playlist)
    - [2.2.3. TOTAL](#223-total)
    - [2.2.4. 플리의 공개/비공개](#224-플리의-공개비공개)
    - [2.2.5. 삭제 예정 플리](#225-삭제-예정-플리)
  - [2.3 이미지](#23-이미지)
- [3. USER](#3-user)
  - [3.1. 개요](#31-개요)
  - [3.2. 이용](#32-이용)
    - [3.2.1. 회원가입](#321-회원가입)
- [4. PLAYLIST](#4-playlist)
  - [4.1. 개요](#41-개요)
    - [4.1.1. 타입](#411-타입)
      - [4.1.1.1. 타입의 전환](#4111-타입의-전환)

## 1.2 용어의 정의

|용어|단축어|동의어|의미|
|:--|:--:|:--:|:--:|
|유저|-|User, 이용자, 회원, 사용자|이 서비스를 이용하는 자|
|플레이리스트|plylst, 플리|음악을 모아둔 목록, 이 서비스 상에서 공유/청취할 수 있는 것|

## 1.3 DEV ROADMAP

## 1.4 정책

### 1.4.1 개발

### 1.4.2 운영

# 2. DATA

## 2.1. 개요

## 2.2. 형식

### 2.2.1. USER

- <user_id>.json

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
        ],
        "bookmark" : [
            "uuid",
            "uuid",
        ]
    }
```

### 2.2.2. PLAYLIST

- <playlist_uuid>.json

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

### 2.2.3. TOTAL

- total_<day/week/month/all>.json

각 total_day.json / total_week.json / total_month.json / total_all.json 으로 존재함.  

```json
    {
        "is_sort" : false, // 플리의 순위가 매겨졌는지 여부
        "rank" : {
            // "순위": {"uuid" : "score"}
        }
    }
```

### 2.2.4. 플리의 공개/비공개

- visibility_playlist.json

```json
    {
        "public" : ["uuid" ... "uuid"],
        "public_to_private" : ["uuid" ... "uuid"],
        // "private_to_public" : ["uuid" ... "uuid"] 은 없고 바뀌면 바로 public 에 추가됨
    }
```

### 2.2.5. 삭제 예정 플리

- BeDeleted.json

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

## 2.3 이미지

# 3. USER

## 3.1. 개요

## 3.2. 이용

### 3.2.1. 회원가입

# 4. PLAYLIST

## 4.1. 개요

### 4.1.1. 타입

1. 기본 타입

|타입|설명|비고|
|:--:|:--:|:--:|
|공개|집계 시스템에 포함되지 않는 플리||
|비공개|||

2. 기타 타입

|타입|설명|비고|
|:--:|:--:|:--:|
|저장||
|공식||

#### 4.1.1.1. 타입의 전환
