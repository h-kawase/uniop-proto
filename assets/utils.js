function loadScript(url, callback) {
    // Adding the script tag to the head as suggested before
    var head = document.head;
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;

    // Then bind the event to the callback function.
    // There are several events for cross browser compatibility.
    script.onreadystatechange = callback;
    script.onload = callback;

    // Fire the loading
    head.appendChild(script);
}

loadScript("./leader-line.min.js", function () { });

function write_line(from_, to_) {
    {
        if (LeaderLine !== undefined) {
            new LeaderLine(
                document.getElementById(from_),
                document.getElementById(to_),
                {
                    path: 'grid',
                    startSocket: 'bottom',
                    endSocket: 'top',
                    startPlug: 'behind',
                    endPlug: 'behind',
                    color: 'rgba(128, 128, 128, 0.5)'
                },
            );
        }
    }
}