<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nama Mas'ud</title>
</head>
<body>
    <button id="showName">Tampilkan Nama</button>

    <script>
        document.getElementById('showName').addEventListener('click', function() {
            alert('Nama saya adalah Mas\'ud');
        });
    </script>
</body>
</html>



<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nama Mas'ud</title>
    <style>
        .name {
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            color: #333;
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div class="name" id="displayName"></div>

    <script>
        document.getElementById('displayName').textContent = 'Nama saya adalah Mas\'ud';
    </script>
</body>
</html>


      <!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Validasi Nama</title>
</head>
<body>
    <label for="nameInput">Masukkan Nama:</label>
    <input type="text" id="nameInput">
    <button id="checkName">Periksa Nama</button>
    <p id="result"></p>

    <script>
        document.getElementById('checkName').addEventListener('click', function() {
            var nameInput = document.getElementById('nameInput').value;
            var result = document.getElementById('result');
            if (nameInput === 'Mas\'ud') {
                result.textContent = 'Nama yang dimasukkan adalah Mas\'ud';
                result.style.color = 'green';
            } else {
                result.textContent = 'Nama yang dimasukkan bukan Mas\'ud';
                result.style.color = 'red';
            }
        });
    </script>
</body>
</html>

