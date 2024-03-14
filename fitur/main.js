// Menampilkan formulir pemesanan
function tampilkanFormulir() {
    var form = document.getElementById("orderForm");
    form.style.display = "block";
  
    var tombolPesan = document.getElementById("pesanButton");
    tombolPesan.disabled = true; // Menonaktifkan tombol setelah diklik
  }
  
  // function tampilkanBeranda(){
  //   alert("Berhasil");
  // }
  
  function submitForm(event) {
    event.preventDefault(); // Mencegah pengiriman formulir yang default
    alert("Formulir berhasil disubmit!");
  
    // Membersihkan nilai input formulir
    document.getElementById("nama").value = "";
    document.getElementById("alamat").value = "";
    document.getElementById("telepon").value = "";
  }