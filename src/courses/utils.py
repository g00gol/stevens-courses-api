from scrapy import Selector
import re
from courses.schemas import ClassPage, Class


def parse_course(page: ClassPage) -> Class:
    html = Selector(text=page.text)
    main = html.css("#main")

    id = main.css("h1 span::text").get()
    # get the text right next to the span tag
    name = "".join([t.strip() for t in main.css(
        "h1 span::text").css("*::text").getall()[1:]]).strip()

    description = " ".join(main.css(".desc::text").getall()).strip()
    credits = main.css(".sc_credits .credits::text").get() or "0"
    prerequisites = " ".join(
        main.css(".sc_prereqs::text").getall()).strip()
    offered = main.css("#offered::text").getall()
    cross_listed = main.css(
        ".sc_credits + h3 + a.sc-courselink::text").getall()
    distribution = main.css("#distribution::text").getall()
    link = page.link

    return Class(
        id=id,
        name=name,
        description=description,
        credits=credits,
        prerequisites=prerequisites,
        offered=offered,
        cross_listed=cross_listed,
        distribution=distribution,
        link=link,
    )
