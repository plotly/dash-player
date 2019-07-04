.dashPlayer_js_metadata <- function() {
deps_metadata <- list(`dash_player` = structure(list(name = "dash_player",
version = "0.0.1", src = list(href = NULL,
file = "deps"), meta = NULL,
script = 'dash_player.min.js',
stylesheet = NULL, head = NULL, attachment = NULL, package = "dashPlayer",
all_files = FALSE), class = "html_dependency"))
return(deps_metadata)
}

dash_assert_valid_wildcards <- function (attrib = list("data", "aria"), ...)
{
    args <- list(...)
    validation_results <- lapply(names(args), function(x) {
        grepl(paste0("^", attrib, "-[a-zA-Z0-9]{1,}$", collapse = "|"),
            x)
    })
    if (FALSE %in% validation_results) {
        stop(sprintf("The following wildcards are not currently valid in Dash: '%s'",
            paste(names(args)[grepl(FALSE, unlist(validation_results))],
                collapse = ", ")), call. = FALSE)
    }
    else {
        return(args)
    }
}
