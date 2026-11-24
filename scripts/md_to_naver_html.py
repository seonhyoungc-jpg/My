#!/usr/bin/env python3
"""final_post.md -> 네이버 에디터 붙여넣기용 HTML 변환기.

네이버 스마트에디터는 마크다운을 해석하지 않지만, 브라우저에서 복사한
서식 있는 텍스트(리치 텍스트)는 표·굵게·소제목까지 그대로 받아들인다.
그래서 발행용 본문만 뽑아 HTML로 렌더한 뒤, 브라우저에서 전체 복사해
붙여넣는 방식을 쓴다.

사용: python3 scripts/md_to_naver_html.py <final_post.md> <출력.html>
"""
import html
import re
import sys


def extract_body(md: str) -> str:
    """발행용 본문만 추출 (─── 구분선 사이, 체크리스트 제외)."""
    parts = md.split("───────────────────────────────")
    if len(parts) >= 3:
        return parts[1].strip()
    # 구분선이 없으면 제목 줄 이후 전체
    return md.split("\n", 1)[1].strip() if "\n" in md else md


def inline(text: str) -> str:
    """인라인 마크업 변환 (이스케이프 후 처리)."""
    out = html.escape(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\w)\[(.+?)\](?!\()", r"<strong>\1</strong>", out)  # [내부링크 제목]
    out = re.sub(r"`(.+?)`", r"<code>\1</code>", out)
    # 맨 URL을 실제 링크로 (복사해 붙여도 네이버가 링크로 인식하도록)
    out = re.sub(
        r"(?<!['\"=>])(https?://[^\s<>\"']+)",
        r'<a href="\1">\1</a>',
        out,
    )
    return out


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def convert(body: str) -> str:
    lines = body.split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        s = line.strip()

        if not s:
            i += 1
            continue

        # 표
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            header = split_row(s)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i].strip()))
                i += 1
            out.append("<table border='1' cellpadding='6' cellspacing='0'>")
            out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr></thead>")
            out.append("<tbody>")
            for r in rows:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table>")
            continue

        # 미디어/링크 안내 블록 (> 🖼 / > 🎬 / > 🔗)
        # 링크는 '사진 올리기'와 성격이 다른 작업이라 색을 분리해 눈에 띄게 한다.
        if s.startswith(">") and re.search(r"🖼|🎬|🔗", s):
            cls = "linkbox" if "🔗" in s else "media"
            block = []
            while i < n and lines[i].strip().startswith(">"):
                block.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(
                f"<p class='{cls}'>"
                + "<br>".join(inline(b) for b in block if b)
                + "</p>"
            )
            continue

        # 일반 인용
        if s.startswith(">"):
            block = []
            while i < n and lines[i].strip().startswith(">"):
                block.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote><p>" + "<br>".join(inline(b) for b in block if b) + "</p></blockquote>")
            continue

        # 소제목
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m:
            level = min(len(m.group(1)), 4)
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue

        # 번호 목록
        if re.match(r"^\d+\.\s", s):
            items = []
            while i < n and re.match(r"^\d+\.\s", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s", "", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
            continue

        # 글머리 목록
        if re.match(r"^[-*]\s", s):
            items = []
            while i < n and re.match(r"^[-*]\s", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s", "", lines[i].strip()))
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue

        # 구분선
        if re.match(r"^-{3,}$", s):
            out.append("<hr>")
            i += 1
            continue

        out.append(f"<p>{inline(s)}</p>")
        i += 1

    return "\n".join(out)


TEMPLATE = """<!doctype html>
<meta charset="utf-8">
<title>{title}</title>
<style>
  body {{ font-family: -apple-system, 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
         max-width: 760px; margin: 0 auto; padding: 24px 16px; line-height: 1.75;
         color: #1a1a1a; background: #fff; }}
  .howto {{ background: #fffbe6; border: 1px solid #ffe08a; border-radius: 8px;
           padding: 14px 16px; margin-bottom: 28px; font-size: 14px; }}
  .howto b {{ color: #b45309; }}
  #post h1 {{ font-size: 25px; line-height: 1.4; margin: 0 0 20px; }}
  #post h2 {{ font-size: 20px; margin: 34px 0 12px; }}
  #post h3 {{ font-size: 17px; margin: 24px 0 10px; }}
  #post table {{ border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 15px; }}
  #post th {{ background: #f5f5f5; }}
  #post th, #post td {{ border: 1px solid #ddd; padding: 7px 9px; text-align: left; }}
  #post blockquote {{ border-left: 3px solid #ccc; margin: 16px 0; padding: 2px 0 2px 14px; color: #444; }}
  #post .media {{ background: #eef5ff; border: 1px dashed #8ab4f8; border-radius: 6px;
                 padding: 10px 12px; margin: 18px 0; font-size: 14px; color: #1a4b8c; }}
  #post .linkbox {{ background: #e8f8ee; border: 2px solid #34a853; border-radius: 6px;
                   padding: 12px 14px; margin: 22px 0; font-size: 15px; color: #14612f; }}
  #post li {{ margin: 5px 0; }}
  #post hr {{ border: 0; border-top: 1px solid #e5e5e5; margin: 28px 0; }}
  #post code {{ background: #f3f3f3; padding: 1px 5px; border-radius: 3px; font-size: 14px; }}
</style>

<div class="howto">
  <b>네이버에 올리는 법</b><br>
  1. 이 페이지에서 <b>전체 선택</b>(Ctrl/⌘ + A) → <b>복사</b>(Ctrl/⌘ + C)<br>
  2. 네이버 블로그 글쓰기 열고 <b>붙여넣기</b>(Ctrl/⌘ + V) — 표·굵게·소제목이 그대로 들어갑니다<br>
  3. <span style="color:#1a4b8c">파란 박스</span> 자리 → <b>사진·영상 올리고 박스 삭제</b><br>
  4. <span style="color:#14612f">초록 박스</span> (맨 아래, 마무리 글 다음) → <b>스마트스토어 링크 1개 넣고 박스 삭제</b><br>
  5. 맨 아래 태그 입력 → <b>예약 발행</b><br>
  <span style="color:#b45309">※ 이 안내문은 복사되어도 네이버에서 지우시면 됩니다.</span>
</div>

<div id="post">
<h1>{title}</h1>
{body}
</div>
"""


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]
    md = open(src, encoding="utf-8").read()
    title = md.split("\n", 1)[0].lstrip("# ").strip()
    out = TEMPLATE.format(title=html.escape(title), body=convert(extract_body(md)))
    open(dst, "w", encoding="utf-8").write(out)
    print(f"{dst} 생성 ({len(out):,} bytes)")


if __name__ == "__main__":
    main()
