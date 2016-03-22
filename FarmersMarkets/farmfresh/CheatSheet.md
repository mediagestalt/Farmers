response.xpath('//script').re(r'new google\.maps\.LatLng(\([0-9.]+,-[0-9.]+\))')

#extracts lat / long