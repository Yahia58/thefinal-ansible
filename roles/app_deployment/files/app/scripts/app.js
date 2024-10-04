document.addEventListener('DOMContentLoaded', () => {
    fetch('/databases')
        .then(response => response.json())
        .then(data => {
            const tablesDiv = document.getElementById('tables');
            if (data.error) {
                tablesDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                const tablesList = data.tables.map(table => `<p>${table}</p>`).join('');
                tablesDiv.innerHTML = tablesList || '<p>No tables found.</p>';
            }
        })
        .catch(err => console.error('Error fetching data:', err));
});

$(document).ready(function() {
    $.getJSON('/databases', function(data) {
        console.log(data);  // Log the data to see what is returned
        if (data.error) {
            $('#databases').text(data.error);
        } else {
            let dbHtml = '<ul>';
            data.forEach(function(db) {
                dbHtml += '<li>' + db + 
                ' <button class="show-tables" data-db="' + db + '">Show Tables</button></li>';
            });
            dbHtml += '</ul>';
            $('#databases').html(dbHtml);
        }
    });

    // Event delegation for dynamically created buttons
    $(document).on('click', '.show-tables', function() {
        var dbName = $(this).data('db');
        $.getJSON('/tables/' + dbName, function(data) {
            if (data.error) {
                $('#tables').text(data.error);
            } else {
                let tablesHtml = '<ul>';
                data.forEach(function(table) {
                    tablesHtml += '<li>' + table + '</li>';
                });
                tablesHtml += '</ul>';
                $('#tables').html(tablesHtml);
            }
        });
    });
});

