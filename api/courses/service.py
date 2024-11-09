from fastapi import HTTPException
from scrapy import Selector
import requests

from courses.schemas import ClassPage, Class
from courses.constants import CLASSES_PAGE
from courses.utils import parse_course


async def get_courses(search="cs-computer-science") -> list[Class]:
    try:
        response = requests.get(CLASSES_PAGE)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve classes page")

    classes_page = Selector(text=response.text)
    class_nodes = classes_page.css("#main > ul:nth-child(3) > li")
    links = ["https://stevens.smartcatalogiq.com" +
             node.css("a::attr(href)").get().lower() for node in class_nodes]
    links = [link for link in links if search.lower() in link.lower()]

    responses = []
    for link in links:
        try:
            response = requests.get(link)
            response.raise_for_status()
            # Parse the course
            page = ClassPage(link=link, text=response.text)
            parsed = parse_course(page)
            responses.append(parsed)
        except requests.RequestException as e:
            raise HTTPException(
                status_code=500, detail="Failed to retrieve class page")

    return responses


async def get_course(page: ClassPage) -> Class:
    try:
        return parse_course(page)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Failed to parse class page")
