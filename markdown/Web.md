# HTML 

HTML (HyperText Markup Language)은 웹페이지를 기술하기 위한 마크업 언어이다. 조금 더 자세히 말하면 웹페이지의 내용(content)과 구조(structure)을 담당하는 언어로써 HTML 태그를 통해 정보를 구조화하는 것이다. 현재는 HTML5이 웹 표준이다. 

#### 기본문법

 1. HTML5 문서는 반드시 <!DOCTYPE html>으로 시작하여 문서 형식(document type)을 HTML5로 지정한다.
 2. 실제적인 HTML document은 2행부터 시작되는데 \<html>과 \</html> 사이에 기술한다.
 3. \<head>와 \</head> 사이에는 document title, 외부파일의 참조, metadata의 설정 등이 위치하며 이 정보들은 브라우저에 표시되지 않는다.
 4. 웹브라우저에 출력되는 모든 요소는 \<body>와 \</body> 사이에 위치한다.
 5. HTML 요소는 시작 태그(start tag)와 종료 태그(end tag) 그리고 태그 사이에 위치한 content로 구성된다. HTML document는 요소(Element)들의 집합으로 이루어진다. ex) \<p>Hello\</p>
 6. 요소는 중첩될 수 있다. 즉, 요소는 다른 요소를 포함할 수 있다. 이때 부자관계가 성립된다. 이러한 부자관계로 정보를 구조화하는 것이다.
 7. 어트리뷰트(Attribute 속성)이란 요소의 성질, 특징을 정의하는 명세이다. 요소는 어트리뷰트를 가질 수 있으며 어트리뷰트는 요소에 추가적 정보(예를 들어 이미지 파일의 경로, 크기 등)를 제공한다. 어트리뷰트는 시작 태그에 위치해야 하며 이름과 값의 쌍을 이룬다. (e.g. name=”value”)
 8. 글로벌 어트리뷰트는 모든 HTML 요소가 공통으로 사용할 수 있는 어트리뷰트다. 몇몇 요소에는 효과가 적용되지 않을 수 있지만, 글로벌 어트리뷰트는 대체로 모든 요소에 사용될 수 있다. ex) id, class, hidden, lang, style, tabindex, title
 
### Semantic Web
대부분의 인터넷 사용자는 원하는 정보를 취득하기 위해 Google이나 Naver와 같은 검색사이트를 이용한다. 그렇기때문에 웹사이트는 **검색엔진**에의 노출이 매우 중요하다. 검색엔진은 **로봇**(Robot)이라는 프로그램을 이용해 매일 전세계의 웹사이트 정보를 수집한다.(이것을 **크롤링**이라 하며 검색엔진의 **크롤러**가 이를 수행한다.) 그리고 검색 사이트 이용자가 검색할 만한 키워드를 미리 예상하여 검색 키워드에 대응하는 **인덱스**(색인)을 만들어 둔다.(이것을 **인덱싱**이라 하며 검색엔진의 **인덱서**가 이를 수행한다.) 인덱스를 생성할 때 사용되는 정보는 검색 로봇이 수집한 정보인데 결국 웹사이트의 HTML 코드이다. 즉 검색 엔진은 HTML 코드 만으로 그 의미를 인지하여야 하는데 이때 **시맨틱 요소(Semantic element)**를 해석하게 된다. 그 중 **시맨틱 태그**란 브라우저, 검색엔진, 개발자 모두에게 콘텐츠의 의미를 명확히 설명하는 역할을 한다. **시맨틱 웹**이란 웹에 존재하는 수많은 웹페이지들에 **메타데이터(Metadata)**를 부여하여, 기존의 잡다한 데이터 집합이었던 웹페이지를 ‘의미’와 ‘관련성’을 가지는 거대한 데이터베이스로 구축하고자 하는 발상이다.

### 레이아웃
웹페이지의 레이아웃을 구성하기 위해 공간을 분리할 필요가 있다. 공간을 분할할 수 있는 태그는 div, span, table 등이 있는데, 과거에는 table 태그를 사용하여 레이아웃을 구성하기도 하였으나 모던 웹에서는 주로 div를 사용하여 레이아웃을 구성한다. 그런데 div 태그는 의미론적으로 어떠한 의미도 가지고 있지 않기 때문에 아래와 같이 HTML5에서 새롭게 추가된 시맨틱 태그를 사용하는 것이 더 나은 방법이나 IE에서 작동하지 않기 때문에 주의가 필요하다.    

![레이아웃 이미지](./building-structure.png "레이아웃 이미지")    
     
     
---

# CSS  
**CSS(Cascading Style Sheets)**는 HTML 요소(Element)의 **style(design, layout etc)**을 표현한다. HTML5 이전 버전의 HTML에는 style을 컨트롤할 수 있는 태그(font, center)가 존재하여 CSS가 없이도 어느 정도의 스타일 표현이 가능하였으나 정보와 구조를 담당하는 HTML의 본연의 임무와 동떨어진 기능까지 추가됨으로서 복잡하고 혼란스러운 언어가 되어 버렸다. HTML5에서는 **HTML는 정보와 구조화**, **CSS는 styling의 정의**라는 본연의 임무에 충실한 명확한 구분이 이루어졌다. 

#### 기본문법   


![CSS 이미지](./css-syntax.png "CSS 이미지")  

 1. **셀렉터 (Selector, 선택자)** : 셀렉터는 스타일을 적용하고자 하는 HTML 요소를 선택하기 위해 CSS에서 제공하는 수단이다. 셀렉터에 의해 선택된 특정 HTML 요소를 어떻게 렌더링(Rendering)할 것인지 브라우저에 지시하는 역할을 하는 것을  **Rule Set(또는 Rule)**이라 한다. 이와 같은 Rule Set의 집합을 **스타일시트(Style Sheet)**라 한다. 
 2. **프로퍼티 (Property / 속성)** : 셀렉터로 HTML 요소를 선택하고 {} 내에 프로퍼티(속성)와 값을 지정하는 것으로 다양한 style을 적용할 수 있다. 프로퍼티는 표준 스펙으로 이미 지정되어 있는 것을 사용하여야하며 사용자가 임의로 정의할 수 없다. 여러개의 프로퍼티를 연속해서 지정할 수 있으며 세미콜론(;)으로 구분한다.
 3. **값 (Value / 속성값)** : 프로퍼티의 값은 사용자가 키워드, 크기 단위, 색상 표현 단위 등의 특정 단위를 지정하여야 한다.

HTML은 CSS를 포함할 수 있다. CSS를 가지고 있지 않은 HTML은 브라우저에서 기본으로 적용하는 CSS(user agent stylesheet)에 의해 렌더링된다. CSS와 HTML을 연동하는 방법은 다음과 같다. 

 1. **Link Style** : HTML에서 외부에 있는 CSS 파일을 로드하는 방식이다. 가장 일반적으로 사용된다.
 2. **Embedding Style** : HTML 내부에 CSS를 포함시키는 방식이다. 매우 간단한 웹페이지의 경우는 문제될 것이 없겠지만 Link style을 사용하는 편이 좋다.
 3. **Inline Style** : HTML요소의 style 프로퍼티에 CSS를 기술하는 방식이다. JavaScript가 동적으로 CSS를 생성할 때 사용하는 경우가 있다. 하지만 일반적인 경우 Link style을 사용하는 편이 좋다.
 
모든 웹 브라우저는 디폴트 스타일(브라우저가 내장하고 있는 기본 스타일)을 가지고 있어 CSS가 없어도 작동한다. 그런데 웹브라우저에 따라 디폴트 스타일이 상이하고 지원하는 tag나 style도 제각각이어서 주의가 필요하다. **Reset CSS**는 기본적인 HTML 요소의 CSS를 초기화하는 용도로 사용한다. 즉 브라우저 별로 제각각인 디폴트 스타일을 하나의 스타일로 통일시켜 주는 역할을 한다. 자주 사용되는 Reset CSS로는 Eric Meyer’s reset, normalize.css 등이있다.    


---

# JavaScript

**Javascript**는 HTML, CSS와 함께 웹을 구성하는 요소중 하나로 웹브라우저에서 동작하는 유일한 언어이다. 또한 JavaScript는 멀티-패러다임 언어로 명령형 (imperative), 함수형 (functional), **프로토타입 기반 (prototype-based) 객체지향형 언어**다. Javascript는  Node.js의 등장으로 웹 브라우저를 벗어나 서버 사이드 애플리케이션 개발에서도 사용되는 Full stack 개발 언어가 되었다. Javascript는 interactive한 웹페이지 작성을 가능하게 한다.  
 **브라우저**의 주요 기능은 사용자가 참조하고자 하는 웹페이지를 서버에 요청(Request)하고 응답(Response)을 받아 브라우저에 표시하는 것이다. 브라우저는 서버로부터 html, css, javascript 파일을 응답받는다. html, css 파일은 렌더링 엔진의 HTML 파서와 CSS 파서에 의해 파싱(Parsing)되어 DOM, CSSOM 트리로 변환되고 렌더 트리로 결합된다. HTML 파서는 script 태그를 만나면 DOM 생성 프로세스를 중지하고 자바스크립트 엔진에 제어 권한을 넘긴다. 자바스크립트 엔진의 실행이 완료된 후 브라우저가 중지했던 시점부터 DOM 생성을 재개한다. 이것은 script 태그의 위치에 의해 DOM의 생성이 지연될 수 있음을 의미한다. 그래서 자바스크립트 때문에 웹페이지의 렌더링이 느려질수 있고 DOM이 완성되는 도중 DOM을 조작할 우려가 있어 에러가 발생할 수도 있다. 와 같이 스크립트 로딩 지연으로 인한 병목 현상을 근본적으로 방지하기 위해 HTML5부터 script 태그에 async와 defer 어트리뷰트가 추가되었다.
 
  - **async** : 웹페이지 파싱과 외부 스크립트 파일의 다운로드가 동시에 진행된다. 스크립트는 다운로드 완료 직후 실행된다. IE9 이하 버전은 지원하지 않는다.
  - **defer** : 웹페이지 파싱과 외부 스크립트 파일의 다운로드가 동시에 진행된다. 스크립트는 웹페이지 파싱 완료 직후 실행된다. IE9 이하 버전에서 정상적으로 동작하지 않을 수 있다.

#### 기본문법

 1. 다른 언어와 달리 자바스크립트에서는 블록 유효범위(Block-level scope)를 생성하지 않는다. **함수 단위의 유효범위(Function-level scope)**만이 생성된다.
 2. 변수를 선언할 때 **var** keyword가 사용된다.
 3. 데이터 타입   
		- 기본 자료형 (primitive data type) : Boolean, null, undefined, Number, String, Symbol  
		- Object
 4. 자바스크립트는 자바와는 달리 값의 자료형에 따라 변수에 데이터 타입을 명시하지 않는다.
 5. 한줄 주석은 // 다음에 작성하며 여러 줄 주석은 /*과 */의 사이에 작성한다. 