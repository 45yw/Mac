(function() {
  window.onload = function() {
    var drawButton, onClickDrawButton, parseBin;
    parseBin = function(binText) {
      var i, index, line, lines, result, _i, _len;
      result = [];
      lines = binText.split('\n');
      for (index = _i = 0, _len = lines.length; _i < _len; index = ++_i) {
        line = lines[index];
        i = line.indexOf(1);
        while (i >= 0) {
          result.push([index * 10, i * 10]);
          i = line.indexOf(1, i + 1);
        }
      }
      return result;
    };
    onClickDrawButton = function() {
      var bin, binText, bins, canvas, context, _i, _len, _results;
      canvas = document.getElementById('canvas');
      binText = document.getElementById('bin').value;
      if (canvas.getContext) {
        bins = parseBin(binText);
        context = canvas.getContext('2d');
        _results = [];
        for (_i = 0, _len = bins.length; _i < _len; _i++) {
          bin = bins[_i];
          _results.push(context.fillRect(bin[1], bin[0], 10, 10));
        }
        return _results;
      }
    };
    drawButton = document.getElementById('draw');
    return drawButton.addEventListener('click', onClickDrawButton);
  };

}).call(this);
