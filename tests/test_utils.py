import matplotlib.figure as mpl_fig

import utils


def test_plot_phylogeny_returns_figure():
    lineage = "Eukaryota > Metazoa > Nematoda > Chromadorea"
    fig = utils.plot_phylogeny(lineage)

    assert isinstance(fig, mpl_fig.Figure)


def test_parasite_card_uses_placeholder_if_img_missing(mocker):
    mocker.patch("utils.st.image")
    mocker.patch("utils.st.button", return_value=False)
    mocker.patch("utils.st.dialog")
    mocker.patch("utils.get_ncbi_info", return_value=None)

    data = {
        "description": "Test parasite"
    }

    utils.parasite_card("Test parasite", data)

    assert data["image"] == "images/placeholder.jpg"


def test_get_ncbi_info_no_match(mocker):
    mock_handle = mocker.Mock()
    mock_handle.close.return_value = None

    mocker.patch("utils.Entrez.esearch", return_value=mock_handle)
    mocker.patch("utils.Entrez.read", return_value={"IdList": []})

    result = utils.get_ncbi_info("TestParasite")

    assert result == "No match found in NCBI Taxonomy."
