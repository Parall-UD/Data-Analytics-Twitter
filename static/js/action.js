$(document).ready(function() {
  var popCanvas = $("#popChart");
  var popCanvasDos = $("#popChartDos");
  var popCanvasTres = $("#popChartTres");
  var popCanvasCuatro = $("#popChartCuatro");
  var popCanvasCinco = $("#popChartCinco");
  var popCanvasSeis = $("#popChartSeis");
  var boolPrueba= false;
  var formatoUno='';
  var formatoDos='';
  var formatoTres='';
  var formatoCuatro='';
  var formatoCinco='';
  var formatoSeis='';
  var contadorAnalizar=0;
  var graficoUno;
  var graficoDos;
  var graficoTres;
  var graficoCuatro;
  var graficoCinco;
  var graficoSeis;

  $( "#btnFrase" ).click(function() {
    if (!$('#frase').val()){
      swal({
            title: "Oops!",
            text: "No dejes el espacio en blanco",
            icon: "warning"
          });
    }
    else{
      pal=$('#frase').val();
      $('#terminosAgregados').append($('<option>', {
          value: pal,
          text : pal
      }));
      $('#frase').val('');
    }

  });

    $( "#btnPalabras" ).click(function() {
      if (!$('#pal').val()){
        swal({
              title: "Oops!",
              text: "No dejes el espacio en blanco",
              icon: "warning"
            });
      }
      else{
        pal=$('#pal').val();
        //alert(pal);

        $('#terminosAgregados').append($('<option>', {
            value: pal,
            text : pal
        }));
        $('#pal').val('');
      }

   });
        $( "#btnHashtag" ).click(function() {
          if (!$('#hash').val()){
            swal({
                  title: "Oops!",
                  text: "No dejes el espacio en blanco",
                  icon: "warning"
                });
          }
          else{
            pal=$('#hash').val();
            pal="#"+pal;
            $('#terminosAgregados').append($('<option>', {
                value: pal,
                text : pal
            }));
            $('#hash').val('');
          }

   });

        $( "#btnCuenta" ).click(function() {
          if (!$('#cta').val()){
            swal({
                  title: "Oops!",
                  text: "No dejes el espacio en blanco",
                  icon: "warning"
                });
          }
          else{
            pal=$('#cta').val();
            pal="@"+pal;
            $('#terminosAgregados').append($('<option>', {
                value: pal,
                text : pal
            }));
            $('#cta').val('');
          }

   });

    $('#contact').css("display", "none");


    $( "#btnEnviar" ).click(function() {
      if( !$('#terminosAgregados').has('option').length > 0 ){
        swal({
              title: "Oops!",
              text: "No ingresaste términos para la búsqueda",
              icon: "error"
            });
      }
      else{
        contadorAnalizar++;
        if (contadorAnalizar > 1){

          graficoUno.destroy();
          graficoDos.destroy();
          graficoTres.destroy();
          graficoCuatro.destroy();
          graficoCinco.destroy();
          graficoSeis.destroy();
          $('#zonaAnalisis').hide();

        }

        $('#contactForm').fadeToggle();
        //var context=popCanvas[0].getContext('2d');
        //context.clearRect(0, 0, popChart.width, popChart.height);
        var values = $("#terminosAgregados>option").map(function() { return $(this).val(); });
        var typeFilter = $("#tipoDatos").val();
        var typeSearch = $("input[name='optradio']:checked").val();
        var longitudTerminos=values.length;
        var i;
        var jsonFinal='{ ';
        for (i = 0; i < longitudTerminos; i++) {
          if (i < (longitudTerminos-1)){
            jsonFinal+='"'+i+'" : '+'"'+values[i]+'" , ';
          }
          else{
            jsonFinal+='"'+i+'" : '+'"'+values[i]+'" , ';
          }
        }
        jsonFinal+='"'+(i++)+'" : '+'"'+typeFilter+'" , '+'"'+(i++)+'" : '+'"'+typeSearch+'"';

        jsonFinal+=' }';

        var obj = JSON.parse(jsonFinal);
        $("#terminosAgregados").empty();
        $.ajax({
    			data : obj,
    			type : 'POST',
    			url : '/process'
  		  })

        .done(function(data) {

  			if (data.error) {
          $('#contactForm').fadeToggle();
          swal("Oops!", data.error);
  			}
  			else {
          const xData= data.resultX4;
          const yData = data.resultY4;
          const dataT = xData.map((x, i) => {
            return {
              x: x,
              y: yData[i]
            };
          });
          $('#zonaAnalisis').show();
          $('#contactForm').fadeToggle();
          graficoUno=graficarPalabrasRepetidas(popCanvas,data.resultY1,data.resultX1);
          graficoDos=graficarPalabrasRepetidasPie(popCanvasDos,data.resultY1,data.resultX1);
          graficoTres=graficarHashtagRepetidos(popCanvasTres,data.resultY2,data.resultX2);
          graficoCuatro=graficarHashtagRepetidosPie(popCanvasCuatro,data.resultY2,data.resultX2);
          graficoCinco=graficarHashtagPopularidad(popCanvasCinco,data.resultY3,data.resultX3,'pie');
          graficoSeis=graficaScatter(popCanvasSeis,dataT);
          values=[]
        }
  		  });
      }
      event.preventDefault();
    });

    $( "#btnDelete" ).click(function() {
      terminoEliminar=$('#terminosAgregados').val();
      $("#terminosAgregados option[value='"+terminoEliminar+"']").remove();
    });

    $('[data-toggle="tooltip"]').tooltip();





    $( "#downloadCanvasUno" ).click(function() {
      formatoUno=$("#formatoUno").val();
      download_image("popChart",formatoUno);
    });

    $( "#downloadCanvasDos" ).click(function() {
      formatoDos=$("#formatoDos").val();
      download_image("popChartDos",formatoDos);
    });

    $( "#downloadCanvasTres" ).click(function() {
      formatoTres=$("#formatoTres").val();
      download_image("popChartTres",formatoTres);
    });

    $( "#downloadCanvasCuatro" ).click(function() {
      formatoCuatro=$("#formatoCuatro").val();
      download_image("popChartCuatro",formatoCuatro);
    });

    $( "#downloadCanvasCinco" ).click(function() {
      formatoCinco=$("#formatoCinco").val();
      download_image("popChartCinco",formatoCinco);
    });

    $( "#downloadCanvasSeis" ).click(function() {
      formatoSeis=$("#formatoSeis").val();
      download_image("popChartSeis",formatoSeis);
    });

    $("#resetCanvas").click(function(){
        //Used the [0] to select the correct element in canvas
    context.clearRect(0,0, canvas[0].width, canvas[0].height);
});


});
