
;(function($) {
    'use strict';
    var resizeDone = false;
    var zoomSet = false;

    var googleLoading = false;

    var googleLoaded = function() {
        if (
            typeof google === 'undefined' ||
            typeof google.maps === 'undefined'
        ) {
            return false;
        }

        return true;
    };

    var waitFor = function(condition, callback, time, stop) {
        if (condition()) {
            return callback();
        }

        time = time || 100;
        stop = stop || false;

        var interval = setInterval(function() {
            if (condition()) {
                callback();
                clearInterval(interval);
            }
        }, time);

        if (stop) {
            var timeout = setTimeout(function() {
                clearInterval(interval);
            }, stop);
        }
    };
    var mapType = function(key) {
        var types = google.maps.MapTypeId;

        if (types.hasOwnProperty(key)) {
            return types[key];
        }

        for (var type in types) {
            if (types[type] === key) {
                return key;
            }
        }

        return types.ROADMAP;
    };


    var resetBounds = function(map, bounds, center, zoom) {
        map.fitBounds(bounds);


        if (
            center.hasOwnProperty('lat') &&
            center.hasOwnProperty('lng')
        ) {
            map.addListener('bounds_changed', function() {
                map.setCenter(center);
            });
        }


        if (zoom) {
            map.addListener('bounds_changed', function() {
                if (zoomSet) {
                    return;
                }

                map.setZoom(zoom);
                zoomSet = true;
            });
        }
    };


    var mapifyElement = function(element, settings) {
        var map = new google.maps.Map(element, {
            mapTypeId: mapType(settings.type)
        });
        var bounds = new google.maps.LatLngBounds();

        $.each(settings.points, function(i, point) {
            var position;
            var marker;
            var infoWindow;


            if (
                !point.hasOwnProperty('lat') ||
                !point.hasOwnProperty('lng')
            ) {
                return false;
            }

            position = new google.maps.LatLng({
                lat: point.lat,
                lng: point.lng
            });

            if (point.marker) {
                marker = new google.maps.Marker({
                    map: map,
                    position: position
                });


                if (typeof point.marker === 'string') {
                    marker.setIcon(point.marker);
                }


                if (point.title) {
                    marker.setTitle(point.title);
                }


                if (point.infoWindow) {
                    infoWindow = new google.maps.InfoWindow({
                        content: point.infoWindow
                    });

                    marker.addListener('click', function() {
                        infoWindow.open(map, marker);
                    });
                }
            }


            bounds.extend(position);
        });


        resetBounds(map, bounds, settings.center, settings.zoom);

        if (settings.responsive) {
            $(window).on('resizeDone', function() {
                zoomSet = false;
                resetBounds(map, bounds, settings.center, settings.zoom);
            });
        }


        if (settings.callback) {
            settings.callback(map, bounds, settings);
        }
    };


    var mapify = function(collection, settings) {
        waitFor(googleLoaded, function() {
            collection.each(function(i, element) {
                mapifyElement(element, settings);
            });
        }, 50, 4000);
    };


    $.fn.mapify = function(options) {
        var collection = this;
        var settings = $.extend({
            points: [],
            type: 'roadmap',
            center: false,
            zoom: false,
            responsive: false,
            callback: false
        }, options);


        if (!googleLoaded || !googleLoading) {
            googleLoading = true;

            $.getScript('https://maps.google.com/maps/api/js?language=en', function() {
                mapify(collection, settings);
            });
        } else {
            mapify(collection, settings);
        }
    };


    $(window).on('resize', function() {
        clearTimeout(resizeDone);

        resizeDone = setTimeout(function() {
            $(window).trigger('resizeDone');
        }, 100);
    });
})(jQuery);
