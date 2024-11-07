from __future__ import annotations 
# __future__ -> 최신 문법 적용, annotations -> 타입 힌트의 순환 참조 문제를 해결하고, 런타임 성능을 개선하는 데 사용됨, 
# annotations 를 사용하면, 모든 타입 힌트가 런타임 시점에서 문자열로 저장된다. 이는 런타임 메모리 사용량을 줄이고, 성능을 향상 시켜준다.

from argparse import ArgumentParser 
# 프로그램에 필요한 인자를 사용자 친화적인 명령행 인터페이스로 쉽게 작성하도록 돕는 라이브러리
import base64 
# 파이썬 표준 라이브러리 중 하나로, Base64 인코딩과 디코딩을 수행하는 데 사용된다. Base64 는 바이너리 데이터를 텍스트로 인코딩하는 방법으로, 
# 바이너리 데이터를 문자 데이터로 안전하게 전송하거나 저장할 수 있도록 변환한다.
from collections import OrderedDict 
# 파이썬의 collections 모듈은 내장 자료형인 리스트, 튜플, 딕셔러니 등을 보완하거나 확장된 고급 자료형을 제공한다. 이 모듈은 데이터를 효율적으로 
# 관리하고 조작할 수 있도록 다양한 컨테이너 데이터 타입을 제공한다.
# OrderedDict -> key-value 쌍의 순서를 기억하는 딕셔너리이다. 파이썬 3.7 부터는 일반 딕셔너리도 입력 순서를 보장하지만, OrderedDict 는 특정 순서 기반 작업이 필요한 경우 유용하다.
from collections.abc import Callable
# collections.abs 는 리스트, 딕셔너리, 셋 등 컨테이너 타입이 반드시 구현해야 할 메서드와 속성을 정의합니다.
# Callable -> collections.abs 에 정의된 ABC 로, 호출 가능한(callable) 객체를 나타냅니다. 즉, 함수처럼 () 를 사용하여 호출할 수 있는 모든 객체를 포함합니다.
from io import BytesIO
# 파이썬의 io 모듈은 입출력 작업을 위한 다양한 도구를 제공합니다. 이 모듈은 파일 및 스트림을 다루는 데 사용되며, 텍사스와 바이너리 데이터를 읽고 쓸 수 있는 추상화된 계층을 제공한다.
# BytesIO 는 io 모듈에서 제공하는 클래스 중 하나로, 바이너리 데이터를 메모리 내에서 파일처럼 다룰 수 있게 합니다. 즉, 실제 파일이 아니라 메모리에 있는 바이너리 데이터에 대해 파일과 같은 읽기/쓰기 작업을 수행할 수 있다.
import os
# 파이썬의 os 모듈은 운영 체제와 상호작용을 위한 다양한 기능을 제공한다. 이 모듈은 파일 시스템 작업, 환경 변수 관리, 프로세스 관리 등 운영 체제와 관련된 작업을 수행할 수 있는 기능들을 제공한다.
from pathlib import Path, PurePath
# pathlib 모듈은 파일과 디렉토리 경로를 객체 지향적으로 다룰 수 있도록 설계된 모듈이다. 전통적인 문자열 기반 파일 경로 처리를 보다 직관적이고 안전하게 할 수 있는 방법을 제공한다.
# Path 클래스는 파일 시스템 경로를 다루기 위한 주요 클래스다. 이 클래스는 파일이나 디렉토리 경로를 생성, 조작, 확인하고 파일 시스템 작업(파일 생성, 읽기, 쓰기 등)을 수행할 수 있다.
# PurePath 클래스는 순수 경로 작업을 수행하는 클래스입니다. 파일 시스템에 접근하지 않고 경로를 문자열을 다룰 때 사용된다. 즉, 경로의 논리적 조작만들 위해 설계된 클래스다.
from threading import Lock
# 파이썬의 threading 모듈은 멀티쓰레딩(multi-threading)을 구현할 수 있도록 도와주는 모듈이다. 멀티쓰레딩은 하나의 프로그램에서 동시에 여러 작업을 수행할 수 있도록 하는 기능이다. 이 모듈은 병렬 작업을 관리하고 쓰레드 간 동기화를 처리하는 데 사용된다.
# Lock 클래스는 쓰레드 동기화를 위해 사용되는 기본 도구이다. 여러 쓰레드가 동시에 접근할 수 있는 공유 자원(예: 데이터 구조, 파일 등)에 대한 동시 접근을 방지하고, 하나의 쓰레드만 접근할 수 있도록 제어한다.
from typing import TYPE_CHECKING, Any, Literal
# typing 모듈은 타입 힌팅(Type Hinting)을 지원하는 파이썬 표준 라이브러리이다. 타입 힌팅은 코드에 데이터 유형을 명시하여, 코드의 가독성과 정확성을 높히고, 정적 분석 도구(예: mypy)가 코드의 타입 오류를 검출하는 데 도움을 준다.
# TYPE_CHECKING 은 조건부 타입 힌팅을 위해 사용된다. 런타임 시 타입 힌트 코드의 실행을 방지한다, 이를 통해 타입 힌트가 런타임에 불필요하게 실행되지 않도록 하고, 타입 검사 도구가 정적 타입 검사 시에만 이를 확인할 수 있도록 한다.
# Any 는 모든 타입을 의미한다. 특정 변수나 함수가 어떤 타입이든 받을 수 있음을 명시한다. 타입 검사 도구는 Any 타입을 타입 제약이 없는 값으로 간주하므로, 이 변수의 타입으 어떤 값으로도 변경될 수 있다.
# Literal 은 고정된 값의 집합을 타입으로 정의할 수 있다. 변수나 함수의 인자가 지정된 특정 값들 중 하나여야 함을 명시한다. 이를 통해 리터럴 값으로만 인자나 반환 값을 제한할 수 있다.
import zlib
# zlib 모듈은 데이터 압축 및 압축 해제를 위한 파이썬 표준 라이브러리이다. 이 모듈은 Deflate 알고리즘(즉, gzip 포멧의 핵심 알고리즘)을 사용하여 데이터를 효율적으로 압축하고 해제할 수 있게 해준다.
from PIL import Image, ImageCms
# PIL(Python Imaging Library)은 파이썬에서 이미지 처리를 위한 강력한 라이브러리이다. 그러나 원래의 PIL 은 더 이상 유지보수가 되지 않기 때문에, 이를 대체하는 Pillow 가 개발되었다. Pillow 는 PIL 의 포크(Fork) 버전으로,
# 현대적인 파이썬 버전과 호환되며 더 많은 기능과 버그 수정이 포함되여 있다.
# Image 클래스는 PIL 에서 제공하는 주요 클래스 중 하나로, 이미지 파일을 열고, 처리하며, 조작할 수 있도록 해준다.
# ImageCms 모듈은 컬러 관리 시스템(CMS, Color Management System) 기능을 제공한다. 이는 이미지의 색상 프로파일을 관리하고 변환하는 데 사용된다. 
from flask import Flask, Response, abort, make_response, render_template, url_for, jsonify
# Flask 는 파이썬으로 작성된 마이크로 웹 프레임워크이다. 가벼움과 확장성을 강조하며, 빠르게 웹 어플리케이션을 개발할 수 있도록 도와준다. Flask 는 핵심 기능만 제공하며, 필요에 따라 플러그인과 확장을 추가하여 기능을 확장할 수 있다.
# Flask, Flask 애플리케이션의 핵심 클래스이다. 웹 어플리케이션의 루트 객체로 사용되며, 라우팅, 요청 처리, 설정 등을 관리한다.
# Response 는 HTTP 응답을 구체적으로 제어할 수 있도록 제공하는 클래스이다. 상태 코드, 헤더, 본문 등 응답 메세지를 구성할 수 있다.
# abort 는 특정 HTTP 오류 코드를 반환하여 요청을 중단한다. 일반적으로 잘못된 요청에 대해 404(Not Found), 403(Forbidden), 500(Internal Server Error) 등을 반환할 때 사용된다.
# make_response 는 커스텀 응답을 생성한다. 문자열, HTML 템플릿, JSON 등 다양한 형태로 응답을 구성할 수 있다. Response 객체를 직접 생성하지 않고도 쉽게 응답을 만들 수 있다.
# render_template 는 HTML 템플릿을 렌더링하여 응답으로 반환한다. Flask 는 Jinja2 템플릿 엔진을 사용하며, render_template 을 통해 동적 HTML 페이지를 쉽게 생성할 수 있다.
# url_for 는 Flask 어플리케이션 내의 라우트에 대한 URL 을 생성한다. 하드코딩 대신 라우트 이름을 기반으로 URL 을 생성하여, URL 구조 변경 시 코드 수정 없이 대응할 수 있다.

if TYPE_CHECKING:
    # Python 3.10+
    from typing import TypeAlias #TypeAlias 는 타입 별칭을 정의할 때 사용합니다. 이는 복잡한 타입 정의를 간단한 이름으로 대체하여 코드의 가독성을 높이고 유지보수를 용이하게 해준다.

if os.name == 'nt':
    _dll_path = "C:\\Users\\User\\Downloads\\openslide-bin-4.0.0.6-windows-x64\\openslide-bin-4.0.0.6-windows-x64\\bin"
    if _dll_path is not None:
        with os.add_dll_directory(_dll_path):  # type: ignore[attr-defined,unused-ignore]  # noqa: E501
            import openslide
    else:
        import openslide
else:
    import openslide
    
from openslide import OpenSlide, OpenSlideCache, OpenSlideError, OpenSlideVersionError
# openslide 는 디지털 병리학에서 사용되는 대형 이미지 파일(예: 전 슬라이드 이미지, WSI)을 다루기 위한 오픈소스 라이브러리이다. 이 모듈은 의료 이미지 분석을 위한 고해상도 병리 슬라이드를 다루는데 유용하며, 다양한 이미지 포맷을 지원한다.
# 대형 이미지의 특정 부분을 효율적으로 읽고 처리, 이미지의 다양한 해상도(multi-resolution)를 제공하여 줌 및 스케일링 지원, 다양한 슬라이드 포맷을 지원(svs, ndpi, mrxs 등)
# OpenSlide 객체는 디지털 슬라이드 이미지 파일을 열고 조작할 수 있도록 한다. 슬라이드 이미지의 메타 데이터 읽기, 슬라이드의 특정 영역을 읽어오기, 다양한 해상도에서 이미지 추출.
# OpenSlideCache 는 캐시 관리를 위한 클래스. OpenSlide 는 슬라이드 파일에서 데이터를 효율적으로 읽기 위해 캐싱을 지원하며, 이를 통해 이미지 읽기 속도를 향상시킬 수 있다. 캐시 크기를 설정하거나 관리하는 데 사용된다.
# OpenSlideError 는 기본 예외 클래스로, OpenSlide 사용 중 발생할 수 있는 모든 오류의 기본 클래스이다. 슬라이드를 열거나 조작할 때 발생하는 일반적인 에러를 처리한다.
# OpenSlideVersionError 는 버전 호환성 문제와 관련된 예외이다. OpenSlide 라이브러리의 버전이 지원되지 않거나 호환되지 않는 경우 발생한다.  
from openslide.deepzoom import DeepZoomGenerator
# openslide.deepzoom 은 OpenSlide 라이브러리의 서브모듈로, Deep Zoom 기술을 지원하는 기능을 제공한다. Deep Zoom 은 대형 이미지(예: 병리학 슬라이드)를 효율적으로 탐색할 수 있도록 다단계 줌을 지원하는 기술이다.
# 이를 통해 사용자는 고해상도 이미지를 빠르게 탐색하고 세부적으로 확대할 수 있다.
# DeepzoomGenerator 는 대형 이미지를 타일 기반으로 쪼개어 제공하며, 줌 레벨에 따라 적절한 타일을 효율적으로 생성하고 관리할 수 있게 한다.

SRGB_PROFILE_BYTES = zlib.decompress(
    base64.b64decode(
        'eNpjYGA8kZOcW8wkwMCQm1dSFOTupBARGaXA/oiBmUGEgZOBj0E2Mbm4wDfYLYQBCIoT'
        'y4uTS4pyGFDAt2sMjCD6sm5GYl7K3IkMtg4NG2wdSnQa5y1V6mPADzhTUouTgfQHII5P'
        'LigqYWBg5AGyecpLCkBsCSBbpAjoKCBbB8ROh7AdQOwkCDsErCYkyBnIzgCyE9KR2ElI'
        'bKhdIMBaCvQsskNKUitKQLSzswEDKAwgop9DwH5jFDuJEMtfwMBg8YmBgbkfIZY0jYFh'
        'eycDg8QthJgKUB1/KwPDtiPJpUVlUGu0gLiG4QfjHKZS5maWk2x+HEJcEjxJfF8Ez4t8'
        'k8iS0VNwVlmjmaVXZ/zacrP9NbdwX7OQshjxFNmcttKwut4OnUlmc1Yv79l0e9/MU8ev'
        'pz4p//jz/38AR4Nk5Q=='
    )
)

SRGB_PROFILE = ImageCms.getOpenProfile(BytesIO(SRGB_PROFILE_BYTES))

SRGB_PROFILE = ImageCms.getOpenProfile(BytesIO(SRGB_PROFILE_BYTES))

if TYPE_CHECKING:
    ColorMode: TypeAlias = Literal[
        'default',
        'absolute-colorimetric',
        'perceptual',
        'relative-colorimetric',
        'saturation',
        'embed',
        'ignore',
    ]
    Transform: TypeAlias = Callable[[Image.Image], None]
    
class DeepZoomMultiServer(Flask):
    basedir: Path
    cache: _SlideCache

class AnnotatedDeepZoomGenerator(DeepZoomGenerator):
    filename: str
    mpp: float
    transform: Transform

def create_app(
    config: dict[str, Any] | None = None,
    config_file: Path | None = None
) -> Flask:
    app = DeepZoomMultiServer(__name__)
    app.config.from_mapping(
        SLIDE_DIR='.',
        SLIDE_CACHE_SIZE=10,
        SLIDE_TILE_CACHE_MB=128,
        DEEPZOOM_FORMAT='jpeg',
        DEEPZOOM_TILE_SIZE=254,
        DEEPZOOM_OVERLAP=1,
        DEEPZOOM_LIMIT_BOUNDS=True,
        DEEPZOOM_TILE_QUALITY=75,
        DEEPZOOM_COLOR_MODE='default',
    )
    app.config.from_envvar('DEEPZOOM_MULTISERVER_SETTINGS', silent=True)
    if config_file is not None:
        app.config.from_pyfile(config_file)
    if config is not None:
        app.config.from_mapping(config)
        
    app.basedir = Path(app.config['SLIDE_DIR']).resolve(strict=True)
    config_map = {
        'DEEPZOOM_TILE_SIZE': 'tile_size',
        'DEEPZOOM_OVERLAP': 'overlap',
        'DEEPZOOM_LIMIT_BOUNDS': 'limit_bounds',
    }
    opts = { v: app.config[k] for k, v in config_map.items() }
    app.cache = _SlideCache(
        app.config['SLIDE_CACHE_SIZE'],
        app.config['SLIDE_TILE_CACHE_MB'],
        opts,
        app.config['DEEPZOOM_COLOR_MODE'],
    )
    
    def get_slide(user_path: PurePath) -> AnnotatedDeepZoomGenerator:
        try:
            path = (app.basedir / user_path).resolve(strict=True)
        except OSError:
            abort(404)
        if path.parts[: len(app.basedir.parts)] != app.basedir.parts:
            abort(404)
        try:
            slide = app.cache.get(path)
            slide.filename = path.name
            return slide
        except OpenSlideError:
            abort(404)     
    
    # @app.route('/')
    # def index() -> str:
    #     return "Hello, World!"
    # @app.route('/')
    # def index() -> str:
    #     root_dir=_Directory(app.basedir)
    #     return f"{root_dir}"
    # @app.route('/')
    # def index() -> str:
    #     root_dir=_Directory(app.basedir)
        
    #     return jsonify(root_dir.__dict__) 
    @app.route('/')
    def index() -> str:
        return render_template('files.html', root_dir=_Directory(app.basedir))
        
   
    @app.route('/<path:path>.dzi')
    def dzi(path: str) -> Response:
        slide = get_slide(PurePath(path))
        format = app.config['DEEPZOOM_FORMAT']
        resp = make_response(slide.get_dzi(format))
        resp.mimetype = 'application/xml'
        return resp
    
    return app
    
class _SlideCache:
    def __init__(
        self,
        cache_size: int,
        tile_cache_mb: int,
        dz_opts: dict[str, Any],
        color_mode: ColorMode
    ):
        self.cache_size = cache_size
        self.dz_opts = dz_opts
        self.color_mode = color_mode
        self._lock = Lock()
        self._cache: OrderedDict[Path, AnnotatedDeepZoomGenerator] = OrderedDict()
        try:
            self._tile_cache: OpenSlideCache | None = OpenSlideCache(
                tile_cache_mb * 1024 * 1024
            )
        except OpenSlideVersionError:
            self._tile_cache = None
    
    def get(self, path: Path) -> AnnotatedDeepZoomGenerator:
        with self._lock:
            if path in self._cache:
                slide = self._cache.pop(path)
                self._cache[path] = slide
                return slide
        osr = OpenSlide(path)
        if self._tile_cache is not None:
            osr.set_cache(self._tile_cache)
        slide = AnnotatedDeepZoomGenerator(osr, **self.dz_opts)
        try:
            mpp_x = osr.properties[openslide.PROPERTY_NAME_MPP_X]
            mpp_y = osr.properties[openslide.PROPERTY_NAME_MPP_Y]
            slide.mpp = (float(mpp_x) + float(mpp_y)) / 2
        except (KeyError, ValueError):
            slide.mpp = 0
        slide.transform = self._get_transform(osr)
        
        with self._lock:
            if path not in self._cache:
                if len(self._cache) == self.cache_size:
                    self._cache.popitem(last=False)
                self._cache[path] = slide
            return slide
    
    def _get_transform(self, image: OpenSlide) -> Transform:
        if image.color_profile is None:
            return lambda img: None
        mode = self.color_mode
        if mode == 'ignore':
            return lambda img: img.info.pop('icc_profile')
        elif mode == 'embed':
            return lambda img: None
        elif mode == 'default':
            intent = ImageCms.Intent(ImageCms.getDefaultIntent(image.color_profile))
        elif mode == 'absolute-colorimetric':
            intent = ImageCms.Intent.ABSOLUTE_COLORIMETRIC
        elif mode == 'relative-colorimetric':
            intent = ImageCms.Intent.RELATIVE_COLORIMETRIC
        elif mode == 'perceptual':
            intent = ImageCms.Intent.PERCEPTUAL
        elif mode == 'saturation':
            intent = ImageCms.Intent.SATURATION
        else:
            raise ValueError(f'Unknown color mode {mode}')
        transform = ImageCms.buildTransform(
            image.color_profile,
            SRGB_PROFILE,
            'RGB',
            'RGB',
            intent,
            ImageCms.Flags(0),
        )
        
        def xfrm(img: Image.Image) -> None:
            ImageCms.applyTransform(img, transform, True)
            img.info['icc_profile'] = SRGB_PROFILE_BYTES
        
        return xfrm
    
class _Directory:
    _DEFAULT_RELPATH = PurePath('.')
    
    def __init__(self, basedir: Path, relpath: PurePath = _DEFAULT_RELPATH):
        self.name = relpath.name
        self.children: list[_Directory | _SlideFile] = []
        for cur_path in sorted((basedir / relpath).iterdir()):
            cur_relpath = relpath / cur_path.name
            if cur_path.is_dir():
                cur_dir = _Directory(basedir, cur_relpath)
                if cur_dir.children:
                    self.children.append(cur_dir)
                elif OpenSlide.detect_format(cur_path):
                    self.children.append(_SlideFile(cur_relpath))
                    
class _SlideFile:
    def __init__(self, relpath: PurePath):
        self.name = relpath.name
        self.url_path = relpath.as_posix()

if __name__ == '__main__':
    parser = ArgumentParser(usage='%(prog)s [options] [SLIDE-DIRECTORY]')
    parser.add_argument(
        '-B',
        '--ignore-bounds',
        dest='DEEPZOOM_LIMIT_BOUNDS',
        default=True,
        action='store_false',
        help='display entire scan area',
    )
    parser.add_argument(
        '--color-mode',
        dest='DEEPZOOM_COLOR_MODE',
        choices=[
            'default',
            'absolute-colorimetric',
            'perceptual',
            'relative-colorimetric',
            'saturation',
            'embed',
            'ignore',
        ],
        default='default',
        help=(
            'convert tiles to sRGB using default rendering intent of ICC '
            'profile, or specified rendering intent; or embed original '
            'ICC profile; or ignore ICC profile (compat) [default]'
        ),
    )
    parser.add_argument(
        '-c', '--config', metavar='FILE', type=Path, dest='config', help='config file'
    )
    parser.add_argument(
        '-d',
        '--debug',
        dest='DEBUG',
        action='store_true',
        help='run in debugging mode (insecure)',
    )
    parser.add_argument(
        '-e',
        '--overlap',
        metavar='PIXELS',
        dest='DEEPZOOM_OVERLAP',
        type=int,
        help='overlap of adjacent tiles [1]',
    )
    parser.add_argument(
        '-f',
        '--format',
        dest='DEEPZOOM_FORMAT',
        choices=['jpeg', 'png'],
        help='image format for tiles [jpeg]',
    )
    parser.add_argument(
        '-l',
        '--listen',
        metavar='ADDRESS',
        dest='host',
        default='127.0.0.1',
        help='address to listen on [127.0.0.1]',
    )
    parser.add_argument(
        '-p',
        '--port',
        metavar='PORT',
        dest='port',
        type=int,
        default=5000,
        help='port to listen on [5000]',
    )
    parser.add_argument(
        '-Q',
        '--quality',
        metavar='QUALITY',
        dest='DEEPZOOM_TILE_QUALITY',
        type=int,
        help='JPEG compression quality [75]',
    )
    parser.add_argument(
        '-s',
        '--size',
        metavar='PIXELS',
        dest='DEEPZOOM_TILE_SIZE',
        type=int,
        help='tile size [254]',
    )
    parser.add_argument(
        'SLIDE_DIR',
        metavar='SLIDE-DIRECTORY',
        type=Path,
        nargs='?',
        help='slide directory',
    )

    args = parser.parse_args()
    config = {}
    config_file = args.config
    for k in dir(args):
        v = getattr(args, k)
        if not k.startswith('_') and v is not None:
            config[k] = v
    app = create_app(config, config_file)

    app.run(host=args.host, port=args.port, threaded=True)                                                                                                                               
