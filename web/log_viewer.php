<?
class IRCLog
{
    public $log_file;
    
    function __construct ($log_file) {
        if (!is_file ($log_file))
            throw new Exception ("Not a valid file");
        $this->log_file = $log_file;
    }
    
    function render ($options = NULL) {
        $lines = file ($this->log_file);
        $grey_dark = "#444444";
        $grey = "#777777";
        $grey_light = "#AAAAAA";
        $white = "#FFFFFF";
        $stripe = 0;  // Use alternating colors

        $pattern = "/\[(.*)\]\t([^:]*):(.*)/";

        // Table header
        $header = <<<EOD
        <table class="log">
            <thead>
                <th class="light-$stripe">Date/Time</th>   
                <th class="dark-$stripe" width="15px" >User</th>   
                <th class="light-$stripe">Message</th>   
            </thead>
            <tbody>
EOD;
        $reply = $header;
        foreach ($lines as $line) { 
            if (!preg_match ($pattern, $line, $matches)) {
                print $line;
                print_r ($matches);
                
                throw new Exception ("Invalid logfile.");
            }
            if ($stripe == 1)
                $stripe = 0;
            else 
                $stripe = 1;
            
            $entry = <<<EOD
            <tr>
                <td class="light-$stripe">$matches[1]</td>   
                <td class="dark-$stripe">$matches[2]</td>   
                <td class="light-$stripe">$matches[3]</td>   
            </tr>
EOD;
            $reply .= $entry;
        }
        $footer = <<<EOD
            </tbody>
        </table>
EOD;
        $reply .= $footer;
        return $reply;
    }
};

$log_file = "#iitm-linux.log";
$log = new IRCLog($log_file);
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml">
<html>
    <head>
        <title>Rob0tnik - Logs</title>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <h1>Rob0tnik - Logs</h1>

        <?=$log->render()?>

    </body>
</html>

