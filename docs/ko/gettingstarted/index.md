Forge로 시작하기{#Getting Started with Forge}
==========================


기본 모드를 생성하는 가이드 문서입니다. 이 페이지의 나머지는 방향성에 대한 것입니다.




0부터 모딩까지{#From Zero to Modding}
--------------------

1. JDK 17과 JVM 64-bit 버전을 받습니다. 
마인크래프트와 마인크래프트 Forge는 모두 Java 17로 컴파일 하며 개발도 마찬가지입니다. 
32-bit JVM을 사용하면 아래의 gradle task들을 실행할 때 문제가 생길 수 있습니다. 
다음 중 하나를 받으면 됩니다. [Eclipse Adoptium][jdk].  

2. Forge 사이트에서 MDK (Mod Development Kit) 를 받으세요. [MDK download][files]  

3. 다운받은 MDK를 빈 폴더에서 압축을 푸세요. `src/main/java` 경로에 예제 모드에 대한 파일들이 있는 걸 확인하세요. 그 파일 중 모드 개발에 필요한 파일은 일부입니다. 아마 당신의 프로젝트에서 몇몇 파일을 재사용할 수 있을 거에요.  파일 목록은 아래와 같습니다.  
    * `build.gradle`
    * `gradlew.bat`
    * `gradlew`
    * `settings.gradle`
    * the `gradle` folder
    
4. 위 목록의 파일들을 새 폴더로 이동하세요. 이 폴더가 당신의 모드 프로젝트 폴더가 될 겁니다.

5. IDE를 선택하세요:
    * Forge는 오직 Eclipse로 개발하는 것을 권장하지만(only explicitly supports), IntelliJ IDEA나 Visual Studio Code environments를 사용할 수도 있습니다. 하지만 Netbeans부터 vim/emacs에 이르기까지 어느 환경이든 동작해야 합니다. 
    * Eclipse와 Intellij IDEA 모두, 각자의 Gradel integration이 나머지 초기 workspace 설정을 처리할 겁니다. 이것은 Mojang, MinecraftForge, 몇몇 sharing 사이트에 있는 소프트웨어 패키지를 다운받는 것을 포함합니다. VSCode의 경우, 'Gradel Tasks' 플러그인이 초기 workspace 설정을 하는데에 사용될 겁니다.
    * build.gradle 파일의 변경 사항을 적용하려면 (전부는 아니지만 대부분) Gradle을 호출하여 프로젝트를 re-evaluate해야 합니다. 위의 두 IDE 모두 Gradel 패널에 있는 'Refresh' 버튼으로 가능합니다.
    
6. IDE 시작/실행 설정하기:
    * Eclipse의 경우, `genEclipseRuns` gradle task (`gradlew genEclipseRuns`)를 실행합니다. 이것은 시작 설정(Launch Configurations)을 하고 게임을 실행하는 데에 필요한 자산(asset)을 다운로드 할 겁니다. 이 작업이 끝나면 당신의 프로젝트를 refresh하세요.
    * IntelliJ의 경우, `genIntellijRuns` gradle task (`gradlew genIntellijRuns`)를 실행합니다. 이것은 시작 설정(Launch Configurations)을 하고 게임을 실행하는 데에 필요한 자산(asset)을 다운로드 할 겁니다. 만약 "module not specified"라는 에러가 발생했다면, 두 가지 방법이 있습니다. "main" 모듈을 선택하는 설정(configuration)을 수정하거나 `ideaModule` 프로퍼티를 통해 명시(specify)하면 됩니다.
    * VSCode의 경우, `genVSCodeRuns` gradle task (`gradlew genVSCodeRuns`)를 실행합니다. 이것은 시작 설정(Launch Configurations)을 하고 게임을 실행하는 데에 필요한 자산(asset)을 다운로드 할 겁니다.  



Mod 정보 수정하기{#Customizing Mod Information}
--------------------------------

`build.gradle` 파일을 수정하면 당신의 모드가 어떻게 만들어졌는지 수정(customize) 할 수 있습니다. (파일 이름, 버전, 그 외 등등).
 `build.gradle` 안에 있는 대부분은 지우거나 수정할 수 있습니다.  


!!! 중요
    `settings.gradle`을 **수정하지 마세요**. 정확하게 어떤 것인지 모른다면요. default 텍스트는 ForgeGradle 플러그인을 얻는데에 꼭 필요합니다.

 

### Simple `build.gradle` Customizations - 간단한 `build.gradle` 커스텀하기


이 커스텀들은 모든 프로젝트에 권장합니다.  

* 파일 이름 변경 - `archivesBaseName` 값을 프로젝트에 맞게 수정
* "maven coordinates" 변경 - `group` 수정'
* 버전 숫자 변경 - `version` 수정
* 실행 설정 수정 - 모든 `examplemod`를 당신의 모드의 모드 id에 맞게 수정



### Migration to Mojang's Official Mappings - Mojang의 공식 Mapping 합치기

Forge는 Mojang의 공식 Mapping이나 MojMaps을 사용합니다. 
공식 mapping은 class, method, field name을 제공합니다. 파라미터와 javadocs는 이 mapping 세트에 제공되지 않습니다. 
현재 이런 mapping들이 법적으로 안전하다는 보장은 없습니다만, Mojang이 mapping이 쓰이길 원하기 때문에 Forge는 좋은 믿음(?)으로 그들을 받아들이기로 결정했습니다. 
여기서 더 자세한 [Forge의 입장][mojmap]을 읽을 수 있습니다. 




모드 빌드하고 테스트하기{#Building Testing Your Mod}
-----------------------------

1. 모드를 빌드하기 위해, `gradlew build`를 실행하세요. `build/libs` 폴더 아래에 `[archivesBaseName]-[version].jar`라는 이름으로 파일이 생성될겁니다.
이 파일은 Forge가 지원하는 모드로써 `.minecraft`폴더에 있는 `mods` 폴더에 둬서 사용할 수 있고 혹은 배포할 수 있습니다.  

2. 모드를 테스트하는 가장 쉬운 방법은 프로젝트를 설정할때 생성한 실행 구성(run configs)을 사용하는 것입니다. 아니면 `gradlew runClient`을 실행시킬 수도 있습니다. 
실행설정(run configurations) 안에 설정된 모든 소스 집합(any source set)에서 모드의 코드(mod's code)들과 함께 `<runDir>` 위치에서 마인크래프트를 실행할겁니다. 
default MDK는 `main` 소스 집합을 가지고 있기 때문에 `src/main/java` 안에서 작성도닌 모든 코드는 적용될 겁니다.  

3. 서버 실행 구성(run config)을 사용하거나 `gradlew runServer`를 통해 전용 서버를 실행할 수도 있습니다. 이것은 GUI와 함께 마인크래프트 서버를 실행할 겁니다. 
첫 실행 이후, 서버는 바로 꺼질겁니다.(셧다운 될겁니다) `run/eula.txt` 파일을 수정해 마인크래프트 EULA를 허용해주어야 합니다. 한 번 허용하면 서버는 로드되고 `localhost`에 직접 연결하여 접근할 수 있습니다.  



!!! 메모
    만약 전용 서버에서 모드를 사용한다면 그 서버에서 테스트 하는게 좋습니다. (=사용환경과 테스트 환경을 일치시키는 게 좋습니다.)
    
    
    
[files]: https://files.minecraftforge.net "Forge Files distribution site"
[jdk]: https://adoptium.net/temurin/releases?version=17 "Temurin 17 Prebuilt Binaries"
[mojmap]: https://github.com/MinecraftForge/MCPConfig/blob/master/Mojang.md
