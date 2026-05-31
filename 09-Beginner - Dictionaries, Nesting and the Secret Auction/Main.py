# capitals={
#     "France":"Paris",
#     "Germany":"Berlin",
# }
# travel_log={
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"],
# }
# print(travel_log["France"][1])

# nested_list=["A","B",["C","D"]]
# print(nested_list[2])


travel_log={
    "France":{
        "num_times_visited":8,
        "cities_visited":["Paris","Lille","Dijon"]
    },
    "Germany":{
        "cities_visited":["Stuttgart","Berlin"],
        "totale_visits":5},
}
print(travel_log["Germany"]["cities_visited"][1])