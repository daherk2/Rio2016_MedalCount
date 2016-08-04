# -*- coding: utf-8 -*-
import requests
import re

headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) " +
                          "AppleWebKit/537.36 (KHTML, like Gecko)" +
                          " Chrome/52.0.2743.82 Safari/537.36",
}

Info = requests.get("https://www.google.co.in/search?async=hl:en," +
                    "ofr:%5B%22%2Fm%2F03tnk7%22%2C1%2C%22m%22%2C1%2Cnull%2Cnull%2Cnull%2Cnull" +
                    "%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull" +
                    "%2C0%5D,stream:%2Fm%2F03tnk7,_fmt:jspb&ved=0ahUKEwiG_IrmpqjOAhWHQY8KHYp6AhgQprYBCCwoCDAA" +
                    "&yv=2&q=%2Fm%2F03tnk7&asearch=lr_oly", headers=headers)

Country_Medal_Regex = re.compile(r'"[\w\s\-\\,\'Ã´]+",\[.,.,.,.]')

Result = Country_Medal_Regex.findall(Info.content)

print "\n".join(Result)
