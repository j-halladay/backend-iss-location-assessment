#!/usr/bin/env python
import requests
import json
import turtle
import time
__author__ = 'j_halladay'


def get_json(url):

    r = requests.get(url)
    dict1 = json.loads(r.text)

    return dict1


def iss_screen(lat, lon, slocation):
    iss_screen = turtle.Screen()
    iss_screen.register_shape("iss.gif")
    iss_station = turtle.Turtle(shape="iss.gif")
    iss_screen.setup(width=720, height=360)
    iss_screen.setworldcoordinates(-360, -180, 360, 180)
    iss_screen.bgpic("map.gif")
    iss_station.color("yellow")
    iss_station.penup()
    iss_station.goto(2*slocation["request"]["longitude"],
                     2*slocation["request"]["latitude"])
    iss_station.pendown()
    iss_station.dot()
    iss_station.write(str(time.ctime(slocation["response"][0]["risetime"])))
    iss_station.penup()
    iss_station.goto(2*lon, 2*lat)

    iss_screen.exitonclick()


def main():
    iss_Location = get_json("http://api.open-notify.org/iss-now.json")
    current_Astronauts = get_json("http://api.open-notify.org/astros.json")
    iss_over_indianapolis = get_json(
        "http://api.open-notify.org/iss-pass.json?lat=39&lon=-86")
    print(iss_over_indianapolis)
    print("Current Astronauts and Craft")
    for item in current_Astronauts["people"]:
        print(item["name"]+", "+item["craft"])
    print("Total Astronauts in space: {}".format(
        current_Astronauts["number"]))
    print("ISS position, lat:{}, long:{}, at time:{}".format(
        iss_Location["iss_position"]["latitude"],
        iss_Location["iss_position"]["longitude"],
        time.ctime(iss_Location["timestamp"])))
    iss_screen(int(float(iss_Location["iss_position"]["latitude"])),
               int(float(iss_Location["iss_position"]["longitude"])),
               iss_over_indianapolis)


if __name__ == '__main__':
    main()
