# Logger - logs directory

- 메모장보다는 Markdown 미리보기가 가능한 Visual Studio Code 나 Github 또는 기타 코드 에디터(마크다운 리더기)로 읽는 것을 추천해요.
- 2023-07-30 폴더와 그 속의 .log 파일들은 테스트로 생성된 파일이에요.

|단계|의미|저장 파일 접두사|조건|
|:--:|:--|:--:|:--:|
|DEBUG|디버그 로그, 프로그램 동작등을 상세히 기록하는 단계|debug_|config.DEBUG = True|
|SET|`DEBUG` 와 `INFO` 사이의 단계로 시작 설정 등을 기록하는 단계|info_|❌|
|INFO|일반적인 정보를 기록하는 단계|info_|❌|
|WARN|잠재적인 문제를 일으킬 수 있는 문제들을 기록하는 단계|warn_|❌|
|ERROR|치명적인 오류, 예기치 못한 오류나 런타임 예외 등을 기록하는 단계|error_|❌|
|CRIT|ERROR 와 마찬가지로 치명적인 오류의 단계이며, 프로그램이 정상적인 동작을 할 수 없으며 즉각 초치해야 되는 오류를 기록하는 단계|error_|❌|

## 디렉토리 구조

- 모든 레벨의 파일이 모두 존재하지 않을 수도 있어요 ☺️

- <`count`> 는 프로그램 몇 번 째 실행되었는지 표시하는 숫자예요.
    </br>
    1. 로그 별로 레벨 접두사 앞에 <`count`>_ 의 형식으로 붙어요.
    2. e.g. `0_info_2023_09_17.log`
    3. <`count`>는 `<int>.count` 파일을 통해서 관리 돼요

    ```bash
    E-MP3
    ├── logs
    │   └── yy-mm-dd
    │       ├── 0.count    
    │       ├── <count>_debug_yy-mm-dd.log
    │       ├── <count>_info_yy-mm-dd.log
    │       ├── <count>_warn_yy-mm-dd.log
    │       └── <count>_error_yy-mm-dd.log
    └── ...
    ```

### ·

#### ··

##### ···

###### from E-MP3/README.md

ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
